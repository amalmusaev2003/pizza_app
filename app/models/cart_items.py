import uuid
from sqlalchemy import Column, DECIMAL, String, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models import *

class CartItems(Base):
    __tablename__ = "cart_items"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_product = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("products.id"))
    id_cart = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("carts.id"))
    quantity = Column(Integer, default=1)
    total_price = Column(DECIMAL(10, 2), nullable=False)

    product = relationship("Products", back_populates="cart_items")
    cart = relationship("Carts", back_populates="items")

    def __repr__(self):
        return f"<CartItems(quantity={self.quantity})>"