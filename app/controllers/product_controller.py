from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
from app.schemas.product_schema import ProductCreate,ProductUpdate
from app.services import product_service


def get_products(db: Session):
    return product_service.get_products(db)

def get_product_Id(db:Session,productId: uuid.UUID):
    return product_service.get_product_Id(db,productId)

def create_product_controller(db:Session,payload:ProductCreate):
    response = product_service.create_product(db,payload)
    return response

def delete_product(db:Session,productId: uuid.UUID):
    response = product_service.delete_product(db,productId)
    return {"message":"Product Deleted Successfully!"}

def update_product(db:Session,productId: uuid.UUID,payload: ProductUpdate):
    response = product_service.update_product(db,productId,payload)
    return {"message":"Product updated Successfully!", "response":response}