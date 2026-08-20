from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
from app.schemas.user_schema import UserCreate, UserUpdate, PasswordUpdate, UsersFilterPayload
from app.services import user_service


def get_users(db:Session,payload:UsersFilterPayload):
    results, count = user_service.get_users(db,payload)
    return results,count

def get_user(db: Session, user_id: uuid.UUID):

    user = user_service.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user

def create_user(db: Session, user: UserCreate):

    new_user = user_service.create_user(db, user)

    if not new_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email already exists"
        )

    return new_user

def update_user_details(db:Session,user_id: uuid.UUID,payload:UserUpdate):

    updatedUser = user_service.update_user_details(db,user_id,payload)

    if updatedUser is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return updatedUser

def delete_user(db: Session, user_id: uuid.UUID):

    user = user_service.delete_user(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }

def updatePassword(db: Session, user_id: uuid.UUID, payload: PasswordUpdate):
    return user_service.update_password(db, user_id, payload)

