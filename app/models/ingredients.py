import uuid
from sqlalchemy import Column, DECIMAL, String
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models import *

'''
Эта и модель ingredient_product нужна для того, чтобы мочь добавлять доп. ингредиенты для 
того или иного продукта.
'''
class Ingredients(Base):
    __tablename__ = "ingredients"
    
    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), default=0.0)

    products = relationship("IngredientProduct", back_populates="ingredient")

    def __repr__(self):
        return f"<Ingredients(name={self.name}, price={self.price})>"