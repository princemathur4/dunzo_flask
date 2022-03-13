from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from modules.common.db_init import db
from modules.common.models import BaseModel
from modules.entities.store.models import Store, MenuItem
from modules.entities.users.models import User


class Cart(BaseModel):
    __tablename__ = "dunzo_cart"

    user_id = db.Column(db.Integer(), ForeignKey(User.id))
    store_id = db.Column(db.Integer(), ForeignKey(Store.id))


class CartItem(BaseModel):
    __tablename__ = "dunzo_cart_items"

    cart_id = db.Column(db.Integer(), ForeignKey(Cart.id))
    menu_item_id = db.Column(db.Integer(), ForeignKey(MenuItem.id))
    quantity = db.Column(db.Integer())
    discount_percentage = db.Column(db.Float(), nullable=True)
