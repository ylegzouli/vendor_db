# from sqlmodel import create_engine, SQLModel
# from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql+asyncpg://postgres:example@db/test_db"

# engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
# )

# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(SQLModel.metadata.create_all)


from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./vendor.db"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    SQLModel.metadata.create_all(bind=engine)
