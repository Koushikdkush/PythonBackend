from fastapi import FastAPI
from app.routes.user_routes import router as user_routes
from app.routes.product_routes import router as product_routes

app = FastAPI(
    title="User Management API",
    description="FastAPI project using dummy data",
    version="1.0.0"
)

app.include_router(user_routes)
app.include_router(product_routes)


# -------------------------
# Home Route
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to User Management API"
    }
