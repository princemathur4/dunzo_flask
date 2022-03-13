from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import ENUM
from modules.common.db_init import db
from modules.common.models import BaseModel

CUSTOMER = "CUSTOMER"
DELIVERY_PERSON = "DELIVERY_PERSON"
USER_TYPES = [CUSTOMER, DELIVERY_PERSON]


class User(BaseModel):
    __tablename__ = "dunzo_user"
    user_type = db.Column(ENUM(*USER_TYPES, name='UserTypes'))
    name = db.Column(db.String(128))


class Role(BaseModel):
    __tablename__ = "dunzo_role"

    rolename = db.Column(db.String(128))


class UserRole(BaseModel):
    __tablename__ = "dunzo_user_role"

    role_id = db.Column(db.Integer(), ForeignKey(Role.id))
    user_id = db.Column(db.Integer(), ForeignKey(User.id))

