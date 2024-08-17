import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated
from typing import List

from app.db_depends import get_db
from app.dao.products import ProductsDAO
from app.schemas.products import SProduct, SNewProduct, SUpdateProduct

router = APIRouter(
    prefix="/products",
    tags=["Меню"]
)

@router.get("")
async def get_all_products(db: Annotated[AsyncSession, Depends(get_db)]) -> List[SProduct]:
    result = await ProductsDAO.find_all(db)
    return [SProduct.model_validate(row) for row in result]

@router.get("/{product_id}")
async def get_product_by_id(db: Annotated[AsyncSession, Depends(get_db)], product_id: uuid.UUID) -> SProduct:
    result =  await ProductsDAO.find_one_or_none(db, id=product_id)
    return SProduct.model_validate(result)

@router.post("")
async def create_product(db: Annotated[AsyncSession, Depends(get_db)], product: SNewProduct):
    product_data = product.model_dump()
    return await ProductsDAO.create(db, **product_data)

@router.patch("/{product_id}")
async def update_product(db: Annotated[AsyncSession, Depends(get_db)], product_id: uuid.UUID, product: SUpdateProduct):
    product_data = product.model_dump(exclude_unset=True)
    return await ProductsDAO.update(db, product_id, **product_data)

@router.delete("/{product_id}")
async def delete_product(db: Annotated[AsyncSession, Depends(get_db)], product_id: uuid.UUID):
    await ProductsDAO.delete(db, product_id)