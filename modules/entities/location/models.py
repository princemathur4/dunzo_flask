from sqlalchemy import ForeignKey
from modules.common.db_init import db
from modules.common.models import BaseModel
from modules.entities.users.models import User


class Location(BaseModel):
    __tablename__ = "dunzo_location"
    latitude = db.Column(db.Float(),)
    longitude = db.Column(db.Float(),)
    city = db.Column(db.String(128))
    state = db.Column(db.String(128))
    pincode = db.Column(db.Integer())
    address_line = db.Column(db.String(256))


class UserLocation(BaseModel):
    __tablename__ = "dunzo_user_location"
    user_id = db.Column(db.Integer(), ForeignKey(User.id))
    location_id = db.Column(db.Integer(), ForeignKey(Location.id))
