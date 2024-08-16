import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from app.db_depends import get_db
from app.dao.products import ProductsDAO
from app.schemas.products import SNewProduct

router = APIRouter(
    prefix="/products",
    tags=["Меню"]
)

@router.get("")
async def get_all_products(db: Annotated[AsyncSession, Depends(get_db)]):
    return await ProductsDAO.find_all(db)

@router.post("")
async def create_product(db: Annotated[AsyncSession, Depends(get_db)], product: SNewProduct):
    product_data = product.model_dump()
    return await ProductsDAO.create(db, **product_data)