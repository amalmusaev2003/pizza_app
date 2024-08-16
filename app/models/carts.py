import uuid
import enum
from sqlalchemy import Column, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models import *

class CartStatusEnum(enum.Enum):
    ACTIVE = 'Активная'
    ORDERED = 'Оформленная'
    ABANDONED = 'Отмененная'

class Carts(Base):
    __tablename__ = "carts"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_user = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("users.id"))
    status = Column(Enum(CartStatusEnum), nullable=False)

    user = relationship("Users", back_populates="carts")
    items = relationship("CartItems", back_populates="cart")
    order = relationship("Orders", uselist=False, back_populates="cart")