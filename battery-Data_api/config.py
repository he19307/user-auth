# config.py
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = "mrfrIMEngCl0pAKqWIIBS_g"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://idan:IDAN_api@127.0.0.1:32000/batterydb'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://idan:IDAN_api@battery_db:3306/batterydb'
    SQLALCHEMY_ECHO = False

