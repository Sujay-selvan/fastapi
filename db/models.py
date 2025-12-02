from sqlalchemy import Column, Integer, String
from db.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    age = Column(Integer,nullable=False)
    phone_number = Column(String(15),unique=True,nullable=False)
    city = Column(String(100),nullable=True)    