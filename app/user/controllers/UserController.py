
from fastapi import Depends
from app.user.entities.UserEntity import UserEntity
from app.user.interactors.UserInteractor import UserInteractor
from app.user.repositories.UserRepository import UserRepository
from app.shared.base.BaseController import BaseController
from config.database_config import Engine

class UserController(BaseController):

    def __init__(self,userInteracotor: UserInteractor = Depends()):
        self.userInteractor = userInteracotor
        self.userRepository = UserRepository(eng=Engine)
    
    def get(self, id: int):
        return self.userInteractor.list_current_user(id, self.userRepository)

    def create(self, user: UserEntity):
        return self.userInteractor.create_user(user, self.userRepository)

        