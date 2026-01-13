from pydantic import BaseModel
from typing import Optional

class ResetPassword(BaseModel):
    user_name: Optional[str] = None
    password: str
    