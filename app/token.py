import datetime
import jwt
from os import environ

def create_token(user):
    token = {
        "username": user["email"],
        "date": str(datetime.datetime.now())
    }

    encoded_token = jwt.encode(payload=token, key=environ.get('SECRET_KEY'), algorithm="HS256")
    return encoded_token
