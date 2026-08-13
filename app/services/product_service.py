from sqlalchemy.orm import Session
from app.models.products_model import Products
from app.schemas.product_schema import ProductCreate,ProductUpdate
from fastapi import HTTPException
import uuid

# get all products
def get_products(db: Session):
    return db.query(Products).all()

# get product by Id
def get_product_Id(db:Session,productId: uuid.UUID):
    return db.query(Products).filter(
        Products.id == productId
    ).first()

# create product
def create_product(db:Session,payload:ProductCreate):

    existingProduct = db.query(Products).filter(
        Products.productName == payload.productName
    ).first()

    if existingProduct:
        raise HTTPException(status_code=400,detail="Product already exists!")

    newProduct = Products(
        productName=payload.productName,
        price=payload.price,
        description=payload.description,
        stock=payload.stock
    )

    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)
    return newProduct

# delete product
def delete_product(db:Session,productId: uuid.UUID):

    try:
        existingProduct = get_product_Id(db,productId)

        if existingProduct is None:
            raise HTTPException(status_code=404,detail="Product not found!")

        db.delete(existingProduct)
        db.commit()
        return existingProduct
    
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500,detail="Failed to update product")



# update product details
def update_product(
    db: Session,
    productId: uuid.UUID,
    payload: ProductUpdate
):
    try:
        product = get_product_Id(db, productId)

        if product is None:
            raise HTTPException(
                status_code=404,
                detail="Product not found!"
            )

        update_data = payload.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)

        return product

    except HTTPException:
        # Keep your intentional 404 response
        raise

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to update product"
        )
    