from fastapi import Depends
from app.user.services.UserServiceImpl import UserServiceImpl
from app.user.entities.UserEntity import UserEntity, UserFromQuery
from app.shared.base.BaseInteractor import BaseInteractor
from typing import List

class UserInteractor(BaseInteractor):

    def __init__(self, userService: UserServiceImpl = Depends()):
        self.userService = userService
    
    def list_all_users(self, userRepository) -> List:
        return self.userService.get_all_users(userRepository)    

    def create_user(self, user, userRepository):
        return self.userService.create_user(user, userRepository)
    
    def list_current_user(self, user_id, userRepository):
        return self.userService.get_user_by_id(user_id, userRepository)

    

    
    
