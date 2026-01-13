from fastapi import APIRouter,HTTPException,Depends
from schemas import auth_schemas
from common_utlis import crud
from db.db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import or_
from model import models
from common_utlis.utils import verify_pwd

router = APIRouter(prefix='/auth',tags=["auth"])

@router.post('/login')
def login(payload: auth_schemas.ResetPassword,db: Session = Depends(get_db)):
    
    filter_condtion = [or_(models.User.email == payload.user_name ,models.User.phone_number == payload.user_name)]
    
    response = crud.get_record(db=db,model=models.User,filters=filter_condtion)
    
    print("response",response)
    
    if not verify_pwd(response.password,payload.password):
        raise HTTPException(status_code=500,detail="wrong user name or password")
        
    return response