from sqlalchemy.orm import Session
from app.models.products_model import Products
from app.schemas.product_schema import ProductCreate
import uuid

def get_products(db: Session):
    return db.query(Products).all()