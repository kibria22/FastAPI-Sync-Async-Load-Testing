from sqlalchemy import Column, Integer, String, VARCHAR
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column('FLD_Blog_ID',Integer, primary_key=True, index=True)
    title = Column('FLD_title',VARCHAR(50))
    body = Column('FLD_body',VARCHAR(200))
