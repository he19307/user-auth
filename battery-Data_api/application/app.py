# application/app.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from .battery_data_api.resources.add_data import AddBatteryData
from .battery_data_api.resources.get_data import GetBatteryData

from .extensions import db,migrate

def create_app():
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    
    
    db.init_app(app)
    migrate.init_app(app, db)
    # Create the Flask-RESTful API instance
    api = Api(app)
    
    api.add_resource(AddBatteryData, '/addbatterydata')
    api.add_resource(GetBatteryData, '/getbatterydata')

    return app

