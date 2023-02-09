
from fastapi import Depends
from app.auth.interactors.AuthInteractor import AuthInteractor

class AuthCrontroller:

    authInteractor:AuthInteractor

    def __init__(self, authInteractor: AuthInteractor = Depends()):
        self.authInteractor = authInteractor
    

    def login(self, user):
        return self.authInteractor.login(user)