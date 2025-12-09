from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI,HTTPException
from users.users import router as user_router
from db.db import Base,engine
import model.models as models
from schemas.schemas import EmailResponse
from service import mail
from template import mail_template

# Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)

@app.post('/check_email')
def check_mail(payload:EmailResponse):
    subject = mail_template.REGISTRATION_SUBJECT
    body = mail_template.BODY.format(user_name=payload.name,your_app_name="sujayApp",temp_password='1234')
    return mail.send_email(to_email=payload.to_email,subject=subject,body=body,email_header="no-reply")
    # return 
    
