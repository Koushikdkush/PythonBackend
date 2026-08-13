from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    salary: float
    address:str
    phoneNumber:str


class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    age: int
    salary: float
    email: EmailStr
    address: str | None = None
    phoneNumber: str | None = None

    class Config:
        from_attributes = True