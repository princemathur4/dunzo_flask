from modules.common.db_init import db
from sqlalchemy import Column, Integer, TIMESTAMP
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.utcnow(), nullable=False)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow(), onupdate=datetime.utcnow(), nullable=False)

    @classmethod
    def new(cls, **kwargs):
        new_obj = cls(**kwargs)
        db.session.add(new_obj)
        return new_obj
