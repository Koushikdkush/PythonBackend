from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models.user_model import User
from app.routes.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    description="A simple API for managing users",
    version="1.0.0"
)
app.include_router(user_router)

# -------------------------
# Home Route
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to User Management API"
    }
