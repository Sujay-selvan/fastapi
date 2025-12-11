from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    name : str 
    phone_number : str
    email: str
    password : str

class UserResponse(BaseModel):
    id : int
    age : int 
    phone_number: str 
    city : str
    
    model_config = {'from_attributes':True}
    
class EmailResponse(BaseModel):
    name: str
    to_email: str
    
class UpdateRequest(BaseModel):
    name : Optional[str] = None 
    age :Optional[ int ] = None
    phone_number : Optional[ str ] = None
    city : Optional[ str ] = None