from fastapi import Depends
from app.shared.utils.oauth2 import CustomOauth

class AuthServiceImpl():  

    def generate_token(self, user, password):
        return CustomOauth.generate_token(user, password)

  

    
    