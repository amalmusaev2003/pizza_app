from pydantic import BaseModel
from typing import Optional

from app.models.enums import CategoryEnum

class SNewProduct(BaseModel):
    name: str
    description: Optional[str]
    category: CategoryEnum 
    price: float