from .models import Store
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def get_stores(db: AsyncSession):
    async with db() as session:
        result = await session.execute(select(Store))
        return result.scalars().all()

async def add_store(db: AsyncSession, store: Store):
    async with db() as session:
        async with session.begin():
            session.add(store)
        await session.commit()

