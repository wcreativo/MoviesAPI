from fastapi import APIRouter
from fastapi.responses import JSONResponse

from schemas.user import User
from utils.jwt_manager import create_token

user_router = APIRouter()


# Login
@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "w.kreativo@gmail.com" and user.password == "password":
        token = create_token(user.dict())
        return JSONResponse(content={"token": token}, status_code=200)
    return JSONResponse({"error": "User credentials invalid!"}, status_code=400)
