from pydantic import BaseModel
from typing import Optional

from app.models.enums import CategoryEnum


class SNewProduct(BaseModel):
    name: str
    description: Optional[str]
    category: CategoryEnum 
    composition: Optional[str]
    price: float

class SProduct(SNewProduct):
    class Config:
        from_attributes = True

class SUpdateProduct(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    category: Optional[CategoryEnum] = None
    composition: Optional[str] = None
    price: Optional[float] = None
