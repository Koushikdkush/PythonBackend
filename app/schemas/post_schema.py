from pydantic import BaseModel, EmailStr
from typing import Optional
from app.schemas.user_schema import UserShape
import uuid

class PostCreate(BaseModel):
    title:str
    user_id:uuid.UUID

class PostResponse(BaseModel):
    id:uuid.UUID
    title:str
    user_id: uuid.UUID

    class Config:
        from_attributes=True

class PostShape(BaseModel):
    id: uuid.UUID
    title:str
    user:UserShape

    class Config:
        from_attributes=True

