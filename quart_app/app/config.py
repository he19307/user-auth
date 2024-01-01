import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    
    # Database connection details (if applicable)
    db_name = os.getenv('MONGODB_DB')
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    auth_source = os.getenv('MONGODB_AUTH_SOURCE')
    host = os.getenv('MONGODB_HOST')
    port = int(os.getenv('MONGODB_PORT'))
    

