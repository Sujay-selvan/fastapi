from sqlalchemy import Column, Integer, String, DateTime
from db.db import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    phone_number = Column(String(15),unique=True,nullable=False) 
    email = Column(String(100),unique=True)
    password = Column(String(100), nullable = True)
    created_at = Column(DateTime, default=datetime.utcnow)