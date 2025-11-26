from fastapi import FastAPI
from users.users import router as user_router
from db import Base,engine
import models

# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
