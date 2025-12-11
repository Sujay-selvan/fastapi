from fastapi import APIRouter
from schemas import schemas

from common_utlis.utils import generate_hash_pwd
router = APIRouter(prefix='/auth',tags=["auth"])
