from sqlalchemy.orm import Session
from app.services import login_service
from app.schemas.user_schema import LoginPayload

def login(db:Session,payload:LoginPayload):
    return login_service.login(db,payload)