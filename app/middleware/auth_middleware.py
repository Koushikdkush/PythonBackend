from fastapi import HTTPException

def my_middleware(roles: list):
    # Middleware logic here
    current_user_role = "Admin"  # This is just a placeholder. In a real application, you would get this from the request or session.
    def middleware_dependency():
        if current_user_role in roles:
            print(f"Middleware executed for roles: {roles}")
        else:
            raise HTTPException(status_code=403, detail="Access denied")
    return middleware_dependency
