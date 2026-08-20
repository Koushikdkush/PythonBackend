from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate,UserUpdate,PasswordUpdate
from app.utils import passwordHash
import uuid
from starlette import status

def get_users(db: Session,isActive: bool = True,page: int = 1,limit: int = 2):

    try:
        start = (page - 1) * limit
        results = ((db.query(User)
                   .filter(User.isActive == isActive)
                   .offset(start)
                   .limit(limit))
                   .all())
        count = len(results)
        return results,count

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def get_user_by_id(db: Session, user_id: uuid.UUID):
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def update_user_details(
    db: Session,
    user_id: uuid.UUID,
    payload: UserUpdate
):
    try:
        user = get_user_by_id(db, user_id)

        if user is None:
            return None

        update_data = payload.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def create_user(db: Session, user: UserCreate):
    try:
        existing_user = (
            db.query(User)
            .filter(User.email == user.email)
            .first()
        )

        if existing_user:
            return None

        hashedPwd = passwordHash.hash_password(user.password)
        new_user = User(
            name=user.name,
            email=user.email,
            age=user.age,
            salary=user.salary,
            address=user.address,
            phoneNumber=user.phoneNumber,
            password=hashedPwd
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

def update_password(db: Session, user_id: uuid.UUID, payload: PasswordUpdate):

   try:
       user = get_user_by_id(db, user_id)
       if user is None:
           raise HTTPException(status_code=404, detail="User not found")

       hashedPwd = passwordHash.hash_password(payload.password)
       setattr(user, "password", hashedPwd)

       db.commit()
       db.refresh(user)
       return {"message": "Password updated"}

   except Exception as e:
       raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


def delete_user(db: Session, user_id: uuid.UUID):

    try:
        user = get_user_by_id(db, user_id)

        if not user:
            return None

        db.delete(user)
        db.commit()

        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

