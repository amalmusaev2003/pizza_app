import uuid
from sqlalchemy import Column, Text, String, Enum, DECIMAL
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models.enums import CategoryEnum
from app.models import *


class Products(Base):
    __tablename__ = "products"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    category = Column(Enum(CategoryEnum), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    sizes = relationship("Sizes", back_populates="product")
    ingredients = relationship("IngredientProduct", back_populates="product")
    cart_items = relationship("CartItems", back_populates="product")

    def __repr__(self):
        return f"<Products(name={self.name}, description={self.description}, category={self.category})>"