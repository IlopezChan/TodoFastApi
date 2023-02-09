import bcrypt
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from config.env_variables import SECRET_KEY, ALGORITHM
from app.user.repositories.UserRepository import UserRepository
from config.database_config import Engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encrypt(password):
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed_pass = bcrypt.hashpw(bytes, salt)
    return hashed_pass

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def validate_user(user):
    repository = UserRepository(Engine)
    new_user = repository.get_by_username_or_email(user)
    if new_user:
        if new_user.Email == user.Email:
            msg = "El Correo se encuentra registrado"
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=msg)
    
        if new_user.UserName == user.UserName:
            msg = "El UserName se encuentra registrado"
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=msg)