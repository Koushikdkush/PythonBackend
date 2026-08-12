from fastapi import HTTPException
from app.models.products_model import ProductsModel
from app.data.products import products_data

def get_all_products_service():
    return products_data