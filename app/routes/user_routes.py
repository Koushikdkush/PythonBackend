from fastapi import APIRouter
from app.controllers import user_controller
from app.models.user_model import UserModel

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
def get_all_users():
    return user_controller.get_all_users_controller()

@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    return user_controller.get_user_by_id_controller(user_id)

@router.post("/")
def create_user(user_data: UserModel):
    return user_controller.create_user_controller(user_data)

@router.put("/{user_id}")
def update_user(user_id: int, user_data: dict):
    return user_controller.update_user_controller(user_id, user_data)

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return user_controller.delete_user_controller(user_id)