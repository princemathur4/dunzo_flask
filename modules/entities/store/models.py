from sqlalchemy import ForeignKey
from modules.common.db_init import db
from modules.common.models import BaseModel
from modules.entities.location.models import Location


class Store(BaseModel):
    __tablename__ = "dunzo_store"
    name = db.Column(db.String(128))
    location_id = db.Column(db.Integer(), ForeignKey(Location.id))


class Item(BaseModel):
    __tablename__ = "dunzo_item"
    item_name = db.Column(db.String(256))
    mrp = db.Column(db.Float())


class MenuItem(BaseModel):
    __tablename__ = "dunzo_menu_item"

    store_id = db.Column(db.Integer(), ForeignKey(Store.id))
    item_id = db.Column(db.Integer(), ForeignKey(Item.id))
    item_price = db.Column(db.Float())
    available_quantity = db.Column(db.Integer())

