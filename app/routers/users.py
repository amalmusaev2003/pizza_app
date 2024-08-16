import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated

from app.db_depends import get_db
from app.schemas.users import SNewUser, SUpdateUser
from app.utils.users import *
from app.dao.users import UsersDAO

router = APIRouter(
    prefix="/users",
    tags=["Пользователи"]
)

@router.get("")
async def get_all_users(db: Annotated[AsyncSession, Depends(get_db)]):
    return await UsersDAO.find_all(db)

@router.get("/{user_id}")
async def get_user_by_id(db: Annotated[AsyncSession, Depends(get_db)], user_id: uuid.UUID):
    return await UsersDAO.find_one_or_none(db, id=user_id)

@router.post("")
async def create_user(db: Annotated[AsyncSession, Depends(get_db)], user: SNewUser):
    user_data = user.model_dump()
    return await UsersDAO.create(db, **user_data)

@router.patch("/{user_id}")
async def update_user(db: Annotated[AsyncSession, Depends(get_db)], user_id: uuid.UUID, user: SUpdateUser):
    user_data = user.model_dump(exclude_unset=True)
    return await UsersDAO.update(db, user_id, **user_data)

@router.delete("/{user_id}")
async def delete_user(db: Annotated[AsyncSession, Depends(get_db)], user_id: uuid.UUID):
    await UsersDAO.delete(db, user_id)