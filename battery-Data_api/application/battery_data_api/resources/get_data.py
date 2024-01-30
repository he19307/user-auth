from flask_restful import Resource, fields, marshal_with
from flask import request
from ..models import BatteryData, db

get_battery_data_fields = {
    'id': fields.Integer(),
    'voltage': fields.List(fields.Float()),
    'current': fields.List(fields.Float()),
    'latitude': fields.List(fields.Float()),
    'longitude': fields.List(fields.Float())
}

class GetBatteryData(Resource):
    @marshal_with(get_battery_data_fields)
    def post(self):
        try:
            data = request.get_json()
            _id = data.get('id')
            if not _id:
                return {'error': 'ID is required'}, 400

            battery_data = BatteryData.query.filter_by(id=_id).all()  # Fetch all records for the ID

            if battery_data:
                data = {
                    'id': _id,
                    'voltage': [record.voltage for record in battery_data],
                    'current': [record.current for record in battery_data],
                    'latitude': [record.latitude for record in battery_data],
                    'longitude': [record.longitude for record in battery_data],
                }
                return data, 200  # Return the formatted data
            else:
                return {'message': 'Battery data not found'}, 404
        except Exception as e:
            return {'error': str(e)}, 500
