from starlette import status
from app.models.user_model import User
from sqlalchemy.orm import Session
from app.schemas.user_schema import LoginPayload
from fastapi import HTTPException
from app.utils.passwordHash import verify_password
from app.utils.tokenGenerator import create_access_token

def login(db:Session, payload: LoginPayload):
    try:
        user = db.query(User).filter(User.email == payload.email).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")

        isPwdValid = verify_password(payload.password, user.password)

        if not isPwdValid:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Incorrect password")

        access_token,refresh_token = create_access_token(data={"sub": str(user.id),"email":user.email})

        return {
            "message": "Login Successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))