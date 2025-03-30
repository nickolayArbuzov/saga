from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.settings import database_connection

async_engine = create_async_engine(database_connection.async_database_url, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

sync_engine = create_engine(database_connection.sync_database_url, future=True)

SessionLocal = sessionmaker(bind=sync_engine, autoflush=False, autocommit=False)

Base = declarative_base()
