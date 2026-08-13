from pydantic import BaseModel
from typing import Optional
import uuid


class ProductCreate(BaseModel):
    productName:str
    price:float
    description:str | None = None
    stock:int | None = None

class ProductUpdate(BaseModel):
    productName:str | None = None
    price:float | None = None
    description:str | None = None
    stock:int | None = None




class ProductResponse(BaseModel):
    id:uuid.UUID
    productName:str
    price:float
    description:str | None = None
    stock:int | None = None

    class Config:
        from_attributes = True