import uuid
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update, insert
from typing import Optional

class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, db: AsyncSession, **filter_by):
        query = select(cls.model.__table__.columns).filter_by(**filter_by) # type: ignore
        result = await db.execute(query)
        return result.mappings().all()
    
    @classmethod 
    async def find_one_or_none(cls, db: AsyncSession, **filter_by):
        query = select(cls.model.__table__.columns).filter_by(**filter_by) # type: ignore
        result = await db.execute(query)
        return result.mappings().one_or_none()
    
    @classmethod
    async def create(cls, db: AsyncSession, **data) -> Optional[dict]:
        await db.execute(insert(cls.model).values(**data)) # type: ignore
        await db.commit()

        return {
            'status_code': status.HTTP_201_CREATED,
            'detail': 'created successfully',
        }

    @classmethod
    async def delete(cls, db: AsyncSession, model_id: uuid.UUID) -> Optional[dict]:
        query = delete(cls.model).where(cls.model.id == model_id) # type: ignore
        await db.execute(query)
        await db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'detail': 'deleted successfully',
        }

    @classmethod
    async def update(cls, db: AsyncSession, model_id: uuid.UUID, **data) -> Optional[dict]:
        if not data:
            return {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'detail': 'no data provided for update'
            }

        query = (
            update(cls.model) # type: ignore
            .where(cls.model.id == model_id) # type: ignore
            .values(**data)  
            .execution_options(synchronize_session="fetch") 
        )

        await db.execute(query)
        await db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'detail': 'updated successfully'
        }

        