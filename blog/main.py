from os import stat
from fastapi import FastAPI, status
from fastapi.param_functions import Body, Depends
from sqlalchemy.sql.functions import mode
from . import models
from .schemas import Blog
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
import threading
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

models.Base.metadata.create_all(engine)

# main.py

loop = asyncio.get_running_loop()
loop.set_default_executor(ThreadPoolExecutor(max_workers=300))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(blog: Blog, db: Session = Depends(get_db)):
    print("count now",threading.active_count())
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    # await asyncio.sleep(2)
    time.sleep(2)
    db.close()
    return new_blog


@app.get('/all')
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}')
def show(id: int, db: Session = Depends(get_db)):
    print("id",id)
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # db.close()
    time.sleep(2)
    # await asyncio.sleep(2)
    return blog
