from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

import os

DB_URL = os.getenv("DB_URL")
# DB_URL=os.getenv('DB_URL')

engine = create_engine(DB_URL,pool_pre_ping=True)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db() -> Session:
    print("DB_URL",DB_URL)
    db = session()
    try:
        yield db
    finally:
        db.close()