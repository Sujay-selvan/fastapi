from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from db import get_db

import schemas

router = APIRouter(prefix='/users',tags=["users"])

@router.get('/users',response_model=schemas.UserResponse)
def get_all_users(request:schemas.UserRequest,db= Depends(get_db)):
    return {
        "message":"all users"
    }
    