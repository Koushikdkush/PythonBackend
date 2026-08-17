from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models.user_model import User
from app.models.products_model import Products
# from app.models.posts_model import Post
from app.routes.user_routes import router as user_router
# from app.routes.product_routes import router as product_router
from app.routes.post_routes import router as post_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Backend System",
    description="Simple apis",
    version="1.0.0"
)
app.include_router(user_router)
# app.include_router(product_router)
app.include_router(post_router)

# -------------------------
# Home Route
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to User Management API"
    }
