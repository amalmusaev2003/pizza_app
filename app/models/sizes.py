import uuid
from sqlalchemy import Column, DECIMAL, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship

from app.db import Base
from app.models import *

class Sizes(Base):
    __tablename__ = "sizes"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id_product = Column(SQLAlchemyUUID(as_uuid=True), ForeignKey("products.id"))
    name = Column(String(255), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    product = relationship("Products", back_populates="sizes")

    def __repr__(self):
        return f"<Sizes(name={self.name})>"