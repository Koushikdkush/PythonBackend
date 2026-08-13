from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from app.controllers import product_controller
import uuid

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/",response_model=list[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return product_controller.get_products(db)

@router.get("/{productId}",response_model=ProductResponse)
def get_product_Id(productId: uuid.UUID,db:Session=Depends(get_db)):
    return product_controller.get_product_Id(db,productId)

@router.post("/createProduct",response_model=ProductResponse)
def createProduct(payload: ProductCreate,db: Session = Depends(get_db)):
    return product_controller.create_product_controller(db,payload)

@router.delete("/{productId}")
def delete_produt(productId: uuid.UUID,db:Session = Depends(get_db)):
    return product_controller.delete_product(db,productId)

@router.patch("/{productId}")
def update_product(productId: uuid.UUID,payload:ProductUpdate,db:Session = Depends(get_db)):
    return product_controller.update_product(db,productId,payload)