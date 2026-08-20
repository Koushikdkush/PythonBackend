from datetime import date
from pydantic import BaseModel, ConfigDict, EmailStr
import uuid

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    salary: float
    address:str
    phoneNumber:str
    password: str

class LoginPayload(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None
    salary: float | None = None
    address: str | None = None
    phoneNumber: str | None = None
    date_of_birth: date | None = None
    idDeleted: bool | None = None
    isActive: bool | None = None


class PasswordUpdate(BaseModel):
    password: str


class UserShape(BaseModel):
    id: uuid.UUID
    name:str
    email:str
    model_config = ConfigDict(from_attributes=True)


class FilteredResponse(BaseModel):
    results: list[UserUpdate]
    count: int

class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    age: int
    salary: float
    email: EmailStr
    address: str | None = None
    phoneNumber: str | None = None
    idDeleted: bool | None = None
    isActive: bool | None = None
    date_of_birth: date | None = None

    class Config:
        from_attributes = True