import jwt
from datetime import datetime, timedelta
from quart import request, jsonify, Blueprint, g
from ..models.model import User, cleanup_expired_temp_users, is_username_taken
from ..config import Config
import phonenumbers
import bcrypt
from quart_rate_limiter import limit_blueprint
from argon2 import PasswordHasher

bp = Blueprint("auth", __name__)
limit_blueprint(bp, 1, timedelta(seconds=10))

ph = PasswordHasher()

@bp.route("/register", methods=["POST"])
async def register():
    data = await request.json

    # Validate user input
    required_fields = ("username", "email", "password", "phone_number", "first_name", "last_name")

    if not all(key in data for key in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    if is_username_taken(data["username"]):
        return jsonify({"error": "Username already exists"}), 400

    try:
        parsed_number = phonenumbers.parse(data["phone_number"], "IN")
        if not phonenumbers.is_valid_number(parsed_number):
            return jsonify({"error": "Invalid phone number"}), 400
    except phonenumbers.phonenumberutil.NumberParseException:
        return jsonify({"error": "Invalid phone number format"}), 400

    # Hash password using Argon2
    hashed_password = ph.hash(data["password"])

    # Store user info in the database
    user = User(
        username=data["username"],
        email=data["email"],
        password=hashed_password,
        phone_number=data["phone_number"],
        first_name=data["first_name"],
        last_name=data["last_name"]
    )

    # Save the user to the database with error handling
    try:
        user.save()
    except Exception as e:
        return jsonify({"error": f"Error saving user: {str(e)}"}), 500

    # Generate JWT token
    expiration_time = datetime.utcnow() + timedelta(hours=1)
    token_payload = {
        "username": data["username"],
        "email": data["email"],
        "phone_number": data["phone_number"],
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "exp": expiration_time.timestamp(),
    }

    jwt_token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({"token": jwt_token}), 201


@bp.route("/profile", methods=["GET"])
async def profile():
    # Check if Authorization header is present
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return jsonify({"error": "Missing Authorization header"}), 401

    # Extract token from Authorization header
    try:
        _, token = auth_header.split()
    except ValueError:
        return jsonify({"error": "Invalid Authorization header format"}), 401

    # Verify and decode the JWT token
    try:
        decoded_token = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401

    # Attach user information to the request context (g object)
    g.user = decoded_token

    # Return user profile information
    return jsonify({
        "username": decoded_token["username"],
        "email": decoded_token["email"],
        "phone_number": decoded_token["phone_number"],
        "first_name": decoded_token["first_name"],
        "last_name": decoded_token["last_name"]
    })


def sanitize_input(input_string):
    # Example using a whitelisting approach
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    sanitized_string = "".join(char for char in input_string if char in allowed_chars)
    return sanitized_string
