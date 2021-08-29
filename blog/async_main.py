from os import stat
from fastapi import FastAPI, status
from fastapi.param_functions import Body, Depends
from sqlalchemy.sql.functions import mode
from . import models
from .schemas import Blog
from .async_database import engine_async, async_session,Base
from sqlalchemy.orm import Session
from sqlalchemy import select
import threading
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

# models.Base.metadata.create_all(engine_async)

# main.py

loop = asyncio.get_running_loop()
loop.set_default_executor(ThreadPoolExecutor(max_workers=300))

async def async_main():
    """Main program function."""

    async with engine_async.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
# class SessionManager:
#     def __init__(self):
#         self.db = SessionLocal()

#     def __enter__(self):
#         return self.db

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.db.close()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
async def create(blog: Blog):
    async with async_session() as db:
        async with db.begin():
            print("count now",threading.active_count())
            new_blog = models.Blog(title=blog.title, body=blog.body)
            db.add(new_blog)
            db.commit()
            db.refresh(new_blog)
            await asyncio.sleep(2)
            # time.sleep(2)
            return new_blog


# @app.get('/all')
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


@app.get('/blog/{id}')
async def show(id: int):
    async with async_session() as db:
        async with db.begin():
            print("id",id)
            # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
            result=await db.execute(select(models.Blog).where(models.Blog.id==id))
            blog=result.scalars().first()
            # db.close()
            # time.sleep(2)
            # db.close()
            await asyncio.sleep(2)
            return blog
