import uuid
from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models import *

class IngredientProduct(Base):
    __tablename__ = "ingredient_product"

    id_product = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey('products.id'), primary_key=True)
    id_ingredient = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey('ingredients.id'), primary_key=True)
    quantity = Column(Integer, default=1)
    is_added = Column(Boolean, default=False)
    is_removable = Column(Boolean, default=False)

    product = relationship("Products", back_populates="ingredients")
    ingredient = relationship("Ingredients", back_populates="products")