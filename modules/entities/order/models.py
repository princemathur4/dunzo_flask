from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from modules.common.db_init import db
from modules.common.models import BaseModel
from modules.entities.store.models import MenuItem, Store
from modules.entities.users.models import User

PAYMENT_PENDING = "PAYMENT_PENDING"
PAYMENT_FAILED = "PAYMENT_FAILED"
CONFIRMATION_PENDING = "CONFIRMATION_PENDING"
ORDER_PLACED = "ORDER_PLACED"
OUT_FOR_DELIVERY = "OUT_FOR_DELIVERY"
ORDER_DELIVERED = "ORDER_DELIVERED"

ORDER_STATES = [
    PAYMENT_PENDING,
    PAYMENT_FAILED,
    CONFIRMATION_PENDING,
    ORDER_PLACED,
    OUT_FOR_DELIVERY,
    ORDER_DELIVERED,
]


class Order(BaseModel):
    __tablename__ = "dunzo_order"

    user_id = db.Column(db.Integer(), ForeignKey(User.id))
    store_id = db.Column(db.Integer(), ForeignKey(Store.id))
    status = db.Column(ENUM(*ORDER_STATES, name='OrderStates'))


PENDING = "PENDING"
DELIVERED = "DELIVERED"
RETURNED = "RETURNED"
ORDER_ITEM_STATES = [
    PENDING,
    DELIVERED,
    RETURNED
]


class OrderItem(BaseModel):
    __tablename__ = "dunzo_order_items"

    order_id = db.Column(db.Integer(), ForeignKey(Order.id))
    menu_item_id = db.Column(db.Integer(), ForeignKey(MenuItem.id))
    quantity = db.Column(db.Integer())
    discount_percentage = db.Column(db.Float(), nullable=True)
    status = db.Column(ENUM(*ORDER_ITEM_STATES, name='OrderItemStates'))
