from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.user_schema import UserCreate, UserResponse,UserUpdate,PasswordUpdate
from app.controllers import user_controller
from app.middleware.auth_middleware import AuthMiddleware
import uuid

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.get("/",dependencies=[Depends(AuthMiddleware)],response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return user_controller.get_users(db)


@router.get("/{user_id}", response_model=UserResponse, dependencies=[Depends(AuthMiddleware)])
def get_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    return user_controller.get_user(db, user_id)


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return user_controller.create_user(db, user)

@router.patch("/update/{user_id}",dependencies=[Depends(AuthMiddleware)], response_model=UserResponse)
def update_user(user_id: uuid.UUID,payload:UserUpdate,db: Session = Depends(get_db)):
    return user_controller.update_user_details(db,user_id,payload)



@router.delete("/{user_id}",dependencies=[Depends(AuthMiddleware)])
def delete_user(
    user_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    return user_controller.delete_user(db, user_id)


@router.patch("/updatePassword/{user_Id}")
def update_password(
        user_Id: uuid.UUID,
        payload:PasswordUpdate,
        db: Session = Depends(get_db)):
    return  user_controller.updatePassword(db,user_Id,payload)
