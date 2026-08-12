from fastapi import FastAPI
from app.routes.user_routes import router as user_routes

app = FastAPI(
    title="User Management API",
    description="FastAPI project using dummy data",
    version="1.0.0"
)

app.include_router(user_routes)


# -------------------------
# Home Route
# -------------------------

@app.get("/")
def home():
    return {
        "message": "Welcome to User Management API"
    }
