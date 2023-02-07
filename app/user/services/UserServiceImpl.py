from fastapi import HTTPException, status
from app.shared.base.BaseService import BaseService
from app.user.repositories.UserRepository import UserRepository
from app.user.entities.UserEntity import UserEntity, UserFromQuery, UserList
from app.user.models.UserModel import User
from app.shared.helpers.token_hash_functions import encrypt
from datetime import datetime

class UserServiceImpl(BaseService):

    def get_user_by_id(self, id: int, repository: UserRepository):
        _user = repository.get_by_id(id)
        print(_user)
        if not _user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

        user = UserFromQuery.from_orm(_user)
        return user

    def get_all_users(self, repository):
        users = repository.get_all()
        return users
            
    def create_user(self, user: UserEntity, repository):
        self.validate_user(user=user, repository=repository)
        password = encrypt(user.Password)
        user.Password = password
        date = datetime.today().strftime('%Y-%m-%d')
        new_user = User(
                Nombre=user.Nombre,
                UserName=user.UserName,
                Email= user.Email,
                Password=user.Password,
                FechaAlta=date
        )
        created_user = repository.create(new_user)
        mapped_user = UserFromQuery.from_orm(created_user)
        return mapped_user
    
    @staticmethod
    def validate_user(user, repository):
        new_user = repository.get_by_username_or_email(user)
        if new_user:
            if new_user.Email == user.Email:
                msg = "El Correo se encuentra registrado"
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=msg)
        
            if new_user.UserName == user.UserName:
                msg = "El UserName se encuentra registrado"
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=msg)
