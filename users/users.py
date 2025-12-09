from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

import schemas.schemas as schemas
from common_utlis import crud
from model import models
from db.db import get_db

router = APIRouter(prefix='/users',tags=["users"])

@router.get('/users')
def get_all_users(db:Session=Depends(get_db)):
    return crud.get_all_record(db,models.User)
            
@router.post('/user')
def insert_single_user(payload:schemas.UserRequest,db:Session = Depends(get_db)):
    return crud.insert_record(db,models.User,payload)

@router.get('/single-user/{user_id}')
def get_single_user(user_id:str,db:Session= Depends(get_db)):
    response = crud.get_single_record(db,models.User,user_id)
    if not response:
        raise HTTPException(status_code=404,detail="user not found")
    return response

@router.put('/update-user/{user_id}')
def update_user(user_id,payload:schemas.UpdateRequest,db:Session = Depends(get_db)):
    return crud.update_record(db,models.User,user_id,payload)
    
@router.delete('/remove-user/{user_id}')
def delete_user(user_id:str,db: Session = Depends(get_db)):
    if not crud.delete_record(db,models.User,user_id):
        raise HTTPException(status_code=500,detail="Error occurs when deleting a record")
    
    return {"message":"successfully deleted a record"}
    