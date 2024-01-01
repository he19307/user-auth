import jwt
from datetime import datetime, timedelta
from quart import request, jsonify, Blueprint
from ..models.model import User, cleanup_expired_temp_users, is_username_taken
from ..config import Config
import phonenumbers
import bcrypt
from quart_rate_limiter import  limit_blueprint
bp = Blueprint("auth", __name__)
limit_blueprint(bp, 1, timedelta(seconds=10))
@bp.route("/register", methods=["POST"])

async def register():
    data = await request.json

    # Validate user input (add more validation as needed)
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

    # Hash password
    hashed_password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
  
    #
    # functions to validate the email and , sanitize_input
    #
	
    #
    # send otp functions implemented should be here with genration 
    #
    
    # Store user info in the database - replace this comment with actual code to save user data
    # For example, assuming you have a User model:
    user = User(
         username=data["username"],
         email=data["email"],
         password=hashed_password,
         phone_number=data["phone_number"],
         first_name=data["first_name"],
         last_name=data["last_name"]
    )
    user.save()  # Save the user to the database
    #cleanup_expired_temp_users()
    # Generate JWT token
    expiration_time = datetime.utcnow() + timedelta(hours=1)  # Expiration time (e.g., 1 hour from now)
    token_payload = {
        "username": data["username"],
        "email": data["email"],
        "phone_number": data["phone_number"],
        "first_name": data["first_name"],
        "last_name": data["last_name"],
        "exp": expiration_time.timestamp(),  # Expiration time in Unix timestamp format
    }

    jwt_token = jwt.encode(token_payload, Config.SECRET_KEY, algorithm="HS256")

    return jsonify({"token": jwt_token}), 201


def sanitize_input(input_string):
    # Example using a whitelisting approach
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    sanitized_string = "".join(char for char in input_string if char in allowed_chars)
    return sanitized_string
