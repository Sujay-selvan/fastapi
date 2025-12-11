from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
# DB_URL=os.getenv('DB_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

def get_db() -> Session:
    db = session()
    try:
        yield db
    finally:
        db.close()