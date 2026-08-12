from fastapi import APIRouter
from app.controllers import product_controller

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/")
def get_all_products():
    return product_controller.get_all_products_controller()