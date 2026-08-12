from app.data.users import users
from fastapi import HTTPException

# get all users
def get_all_users():
    return users

# get user by id
def get_user_by_id(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# create a new user
def create_user(user_data: dict):
    for user in users:
        if user["email"] == user_data["email"]:
            raise HTTPException(status_code=400, detail="Email already exists")
    
    new_id = max(user["id"] for user in users) + 1 if users else 1
    user_data["id"] = new_id
    users.append(user_data)
    return user_data

# update an existing user
def update_user(user_id: int, user_data: dict):
    if "email" in user_data and user_data["email"] is not None:
        raise HTTPException(status_code=400, detail="Email cannot be updated")

    for user in users:
        if user["id"] == user_id:
            user.update(user_data)
            return user
    return None

# delete a user
def delete_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return True
    return False