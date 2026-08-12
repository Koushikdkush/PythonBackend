from fastapi import HTTPException
from app.services import user_service
from app.models.user_model import UserModel

def get_all_users_controller():
    return user_service.get_all_users()

def get_user_by_id_controller(user_id: int):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user_controller(user_data: UserModel):
    return user_service.create_user(user_data.dict())

def update_user_controller(user_id: int, user_data: dict):
    user = user_service.update_user(user_id, user_data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user_controller(user_id: int):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}