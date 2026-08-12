from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app = FastAPI(
    title="User Management API",
    description="FastAPI project using dummy data",
    version="1.0.0"
)


# -------------------------
# Dummy Data
# -------------------------

users = []


# -------------------------
# Request Model
# -------------------------

class User(BaseModel):
    name: str
    age: int
    email: str
    address: str
    skills: list[str]  # Adding a new field for skills


# -------------------------
# Home Route
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to User Management API"
    }

# Request Model for creating a new user

class User(BaseModel):
    name: str
    age: int | None = None
    email: str
    address: str  # Adding a new field for address
    skills: list[str]  # Adding a new field for skills

@app.post("/users")
def create_user(user: User):
    # Check if the email already exists

    if any(existing_user["email"] == user.email for existing_user in users):
        raise HTTPException(status_code=400, detail="Email already exists")
        
    new_user = {
        "id": len(users) + 1,
        **user.dict()
    }
    
    users.append(new_user)
    return new_user

    raise HTTPException(status_code=500, detail="Something went wrong while creating the user")


# get user by id

@app.get("/users")
def get_users():
    if not users:
        raise HTTPException(status_code=404, detail="No users found")   
    return JSONResponse(content=users, status_code=200)
    

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.patch("/users/{user_id}")
def update_user(user_id: int, user_data: User):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user_data.dict().items():
        if value is not None:
            user[key] = value

    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    users.remove(user)
    return {"message": "User deleted successfully"}


# python -m uvicorn app.main:app --reload 