from pydantic import BaseModel
from typing import Optional

class UserRequest(BaseModel):
    name : str 
    age :int
    phone_number : str
    city : Optional[ str ] = None

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