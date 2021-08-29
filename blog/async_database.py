from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
SQLALCHEMY_DATABASE_URL = 'mysql+aiomysql://user:pass@localhost:3306/table'

# engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=True,pool_size=50,max_overflow=50)

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
engine_async = create_async_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=True,pool_size=50,max_overflow=50)

async_session = sessionmaker(
    engine_async,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
)

Base = declarative_base()
