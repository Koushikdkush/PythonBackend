from app.services import product_service
from fastapi import HTTPException


def get_all_products_controller():
    return product_service.get_all_products_service()