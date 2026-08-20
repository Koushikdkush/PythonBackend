from fastapi import Request, HTTPException
from app.utils.tokenGenerator import decode_access_token


def AuthMiddleware(request: Request):

    try:
        print("I am Executing Authorization Middleware")
        authorization = request.headers.get("Authorization")

        if authorization is None:
            raise HTTPException(
                status_code=401,
                detail="Authorization header missing"
            )

        token_type, token = authorization.split(" ", 1)

        if token_type.lower() != "bearer":
            raise ValueError("Invalid Authorization Header")

    except ValueError:
        raise HTTPException(
            status_code=401,
            detail="Invalid Authorization Header"
        )

    payload = decode_access_token(token)
    print(payload)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    request.state.user = payload

    return payload