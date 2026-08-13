from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
import uuid

def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: uuid.UUID):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        return None

    new_user = User(
        name=user.name,
        email=user.email,
        age=user.age,
        salary=user.salary,
        address=user.address,
        phoneNumber=user.phoneNumber
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def delete_user(db: Session, user_id: uuid.UUID):

    user = get_user_by_id(db, user_id)

    if not user:
        return None

    db.delete(user)
    db.commit()

    return user