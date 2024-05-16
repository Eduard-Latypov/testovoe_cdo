from typing import Type
from sqlalchemy import insert, select, delete, update

from database import Base, async_session


class BaseDAO:
    model: Type[Base]

    @classmethod
    async def create(cls, **filter_by):
        async with async_session() as conn:
            stmt = insert(cls.model).values(**filter_by).returning(cls.model.id)
            result = await conn.execute(stmt)
            await conn.commit()
            return result.scalar()

    @classmethod
    async def get_all(cls, **filter_by):
        async with async_session() as conn:
            stmt = select(cls.model).filter_by(**filter_by)
            result = await conn.execute(stmt)
            return result.scalars().all()

    @classmethod
    async def delete(cls, model_id):
        async with async_session() as conn:
            stmt = delete(cls.model).filter_by(id=model_id).returning(cls.model.id)
            result = await conn.execute(stmt)
            id = result.scalar()
            await conn.commit()
            return id

    @classmethod
    async def update(cls, model_id, **filter_by):
        async with async_session() as conn:
            stmt = (
                update(cls.model)
                .where(cls.model.id == model_id)
                .values(**filter_by)
                .returning(cls.model.id)
            )
            result = await conn.execute(stmt)
            await conn.commit()
            return result.scalar()
