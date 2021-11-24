from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from security.functions_jwt import write_token, validate_token
from fastapi.responses import JSONResponse

auth_routes = APIRouter()

class User(BaseModel) :
    username: str
    email: EmailStr

@auth_routes.post("/login")
def login(user: User) :
    # Aca se deberia validar el usuario 
    # contra la base de datos
    print(user.dict())
    if user.username == "martin.ramos" :
        return write_token(user.dict())
    else :
        return JSONResponse(content={"message": "Incorrect user"}, status_code=404)

@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    # print(Authorization)
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)

    