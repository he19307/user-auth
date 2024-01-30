# application/battery_data_api/models.py

from datetime import datetime
from ..extensions import db

class BatteryData(db.Model):

   __tablename__ = "battery_data"
   sr_no = db.Column(db.Integer, primary_key=True, autoincrement=True)
   id = db.Column(db.Integer, nullable=False)
   voltage = db.Column(db.Float, nullable=False)
   current = db.Column(db.Float, nullable=False)
   latitude = db.Column(db.Float, nullable=False)
   longitude = db.Column(db.Float, nullable=False)
   timestamp = db.Column(db.DateTime, default=datetime.utcnow)

   def __repr__(self):
       return f'<BatteryData {self.id}>'
