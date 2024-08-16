import uuid
import enum
from sqlalchemy import Column, ForeignKey, Enum, DECIMAL
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models import *

class OrderStatusEnum(enum.Enum):
    NEW = 'Новый'
    IN_PROGRESS = 'В процессе'
    COMPLETED = 'Завершенный'
    CANCELLED = 'Отменённый'

class Orders(Base):
    __tablename__ = "orders"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_user = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("users.id"))
    id_cart = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("carts.id"))
    status = Column(Enum(OrderStatusEnum), nullable=False)
    total_price = Column(DECIMAL(10, 2), nullable=False)

    user = relationship("Users", back_populates="orders")
    cart = relationship("Carts", back_populates="order")