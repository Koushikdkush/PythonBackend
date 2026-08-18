from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.user_schema import PasswordUpdate, LoginPayload
from app.controllers import login_controller
from uuid import UUID

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/login")
def login_router(payload:LoginPayload, db:Session = Depends(get_db)):
    return login_controller.login(db,payload)