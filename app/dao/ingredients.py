from .base import BaseDAO
from app.models.ingredients import Ingredients

class ProductsDAO(BaseDAO):
    model = Ingredients