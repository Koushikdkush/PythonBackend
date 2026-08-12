from fastapi import FastAPI
from app.routes.user_routes import router as user_routes
from app.routes.product_routes import router as product_routes

app = FastAPI(
    title="User Management API",
    description="FastAPI project using dummy data",
    version="1.0.0"
)

# @app.middleware("http")
# async def log_requests(request, call_next):
#     print(f"Incoming request: {request.method} {request.url}")
#     response = await call_next(request)
#     print(f"Response: {response.status_code}")
#     return response

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
