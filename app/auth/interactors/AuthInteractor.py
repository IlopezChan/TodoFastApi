from fastapi import Depends
from app.auth.services.AuthServiceImpl import AuthServiceImpl
from app.auth.interactors.IAuthInteractor import IAuthInteractor
from app.auth.services.AuthServiceImpl import AuthServiceImpl

class AuthInteractor(IAuthInteractor):

    def __init__(self, authService: AuthServiceImpl = Depends()):
        self.authService = authService

    def login(self, user):
        access_token = self.authService.generate_token(user.username, user.password)        
        return access_token
        
