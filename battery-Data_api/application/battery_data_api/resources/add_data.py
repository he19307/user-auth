#application/battery_data_api/resource/add_data.py
from flask_restful import Resource, fields, marshal_with
from flask import request
from ..models import BatteryData,db

battery_data_fields = {
    'id': fields.Integer(),
    'voltage': fields.Float(),
    'current': fields.Float(),
    'latitude': fields.Float(),
    'longitude': fields.Float()
}

class AddBatteryData(Resource):
    @marshal_with(battery_data_fields)  # Use fields for single values
    def post(self):
        data = request.get_json()

        try:
            battery_data = BatteryData(**data)  # Create a new instance of the model
            db.session.add(battery_data)
            db.session.commit()
            return battery_data, 201  # Return the marshalled data with success status code
        except Exception as e:
            return {'error': str(e)}, 400
