from fastapi import APIRouter, Depends
from app.auth.controllers.AuthController import AuthCrontroller
from app.user.entities.TokenEntity import Token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)

@router.post("/login", response_model=Token)
def login(user: OAuth2PasswordRequestForm=Depends(OAuth2PasswordRequestForm), authController: AuthCrontroller = Depends()):
    return Token(access_token=authController.login(user), token_type="bearer")
