from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class SNewUser(BaseModel):
    name: str
    last_name: Optional[str]
    phone: str
    email: EmailStr
    password: str

class SUpdateUser(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
