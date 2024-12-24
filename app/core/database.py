from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True)
# async_engine = create_async_engine(settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"), echo=True)

Session = sessionmaker(bind=engine, autocommit=False, expire_on_commit=False)
# AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# async def get_async_db():
#     async with AsyncSessionLocal() as session:
#         yield session

db = Annotated[Session, Depends(get_db)]

# async_db = Annotated[AsyncSession, Depends(get_async_db)]
