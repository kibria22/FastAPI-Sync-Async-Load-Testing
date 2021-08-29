from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://user:pass@localhost:3306/table'

engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_pre_ping=True,pool_size=50,max_overflow=50)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
