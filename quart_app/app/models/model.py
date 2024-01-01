from mongoengine import *
from ..config import Config
from datetime import datetime, timedelta 
# Connect to the MongoDB instance with credentials
connect(
    db=Config.db_name,
    username=Config.username,
    password=Config.password,
    authentication_source=Config.auth_source,  # The authentication database (admin in this case)
    host=Config.host,  # Assuming the MongoDB instance is running locally
    port=Config.port,  # Default MongoDB port
)

class User(Document):

    username = StringField(required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    phone_number = StringField(required=True)  # Added for phone number
    first_name = StringField(required=True)  # Added for first name
    last_name = StringField(required=True)  # Added for last name
    #numberotp = StringField(required=True)  # Store the generated OTP
    #emailotp = StringField(required=True)  # Store the generated OTP
    expires_at = DateTimeField(default=datetime.utcnow() + timedelta(minutes=1))  # Set expiration to 1 minute

def is_username_taken(username):
    """
    Check if the username already exists in the database.

    Args:
    - username: The username to check

    Returns:
    - Boolean: True if the username exists, False otherwise
    """
    existing_user = User.objects(username=username).first()
    return existing_user is not None
    
def cleanup_expired_temp_users():
    TempUser.objects(expires_at__lt=datetime.utcnow()).delete()  # Delete expired entries

