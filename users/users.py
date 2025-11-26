from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from db import get_db

router = APIRouter(prefix='/users',tags=["users"])

@router.get('/users')
def get_all_users(db= Depends(get_db)):
    # db = get_db()

    return {
        "message":"all users"
    }
    