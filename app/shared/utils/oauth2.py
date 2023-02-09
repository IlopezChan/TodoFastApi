from fastapi import Depends
from app.shared.exceptions.generic_exceptions import credentials_exception, inactive_user, incorrect_user
from app.user.entities.TokenEntity import TokenData
from datetime import datetime, timedelta
from app.shared.helpers.token_hash_functions import verify_password
from app.user.models.UserModel import User
from app.user.entities.UserEntity import UserIn
from config.env_variables import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import or_
from config.database_config import Engine


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
class CustomOauth():  

    @staticmethod
    def generate_token(username:str, password:str):
        user:UserIn = CustomOauth.authenticate_user(username, password)
        if not user:
            raise incorrect_user
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        return CustomOauth.create_access_token(data = {"sub": user.Email}, expires_delta=access_token_expires)
    
    @staticmethod
    def authenticate_user(username: str, pwd:str):
        user:UserIn = UserIn.from_orm(CustomOauth.get_user(username))
        if not user:
           return False
        if not verify_password(pwd, user.Password):
            return False
        return user
    
    @staticmethod
    def get_user(username: str):
        with Session(Engine) as session:
            user = session.query(User).filter(or_(User.UserName == username,User.Email == username)).first()
            session.close()
            return user

    @staticmethod
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username = payload.get("sub")
            
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
            
        except JWTError:
            raise credentials_exception
        user = CustomOauth.get_user(token_data.username)
        CustomOauth.check_active_user(user)
        
        if user is None:
            raise credentials_exception
        return user

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    def check_active_user(current_user:User):
        if current_user.Estatus.name=="Inactivo":
            raise inactive_user

    
    