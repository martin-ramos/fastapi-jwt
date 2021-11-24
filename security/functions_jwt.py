from logging import exception
from jwt import encode, decode, exceptions
from os import getenv
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2) },
                 key=getenv("SECRET"), algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token, output=False): 
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms=["HS256"])
        decode(token, key=getenv("SECRET"), algorithms=["HS256"])
    except exceptions.DecodeError:
        return JSONResponse(content={"message": "Invalid Token"}, status_code=401)
    except exceptions.ExpiredSignatureError:
        return JSONResponse(content={"message": "Token Expired"}, status_code=401)
    except TypeError:
        print("Hay un error")
