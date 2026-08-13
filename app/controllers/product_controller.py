from fastapi import HTTPException
from sqlalchemy.orm import Session
import uuid
from app.schemas.product_schema import ProductCreate
from app.services import product_service


def get_products(db: Session):
    return product_service.get_products(db)