from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse
from app.controllers import product_controller
import uuid

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/",response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return product_controller.get_products(db)