import uuid
from sqlalchemy import Column, String, TIMESTAMP, func
from sqlalchemy.dialects.postgresql import UUID as SQLAlchemyUUID
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet

from app.db import Base
from app.models import * 

# Генерация ключа шифрования 
key = Fernet.generate_key()
cipher = Fernet(key)

class Users(Base):
    __tablename__ = "users"

    id = Column(SQLAlchemyUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255))
    phone_encrypted = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    carts = relationship("Carts", back_populates="user")
    orders = relationship("Orders", back_populates="user")

    def __repr__(self):
        return f"<User(name={self.name}, last_name={self.last_name}, email={self.email})>"

    @property
    def phone(self):
        return cipher.decrypt(self.phone_encrypted.encode()).decode()

    @phone.setter
    def phone(self, value):
        self.phone_encrypted = cipher.encrypt(value.encode()).decode()