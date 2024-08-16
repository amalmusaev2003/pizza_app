import uuid
from fastapi import status
from sqlalchemy import insert, update
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.utils.users import *
from .base import BaseDAO
from app.models.users import Users

class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def create(cls, db: AsyncSession, **data) -> Optional[dict]:
        if 'password' in data:
            data['password_hash'] = hash_password(data.pop('password'))

        if 'phone' in data:
            data['phone_encrypted'] = encrypt_phone(data.pop('phone'))

        await db.execute(insert(cls.model).values(**data))
        await db.commit()

        return {
            'status_code': status.HTTP_201_CREATED,
            'detail': 'created successfully',
        }
    
    @classmethod
    async def update(cls, db: AsyncSession, user_id: uuid.UUID, **data):
        if not data:
            return {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'detail': 'no data provided for update'
            }
        
        if 'password_hash' in data:
           data['password_hash'] = hash_password(data['password_hash'])

        if 'phone_encrypted' in data:
            data['phone_encrypted'] = encrypt_phone(data['phone_encrypted'])
        
        query = (
            update(cls.model)
            .where(cls.model.id == user_id) 
            .values(**data)  
            .execution_options(synchronize_session="fetch")  
        )

        await db.execute(query)
        await db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'detail': 'updated successfully'
        }