from fastapi import APIRouter, Depends
from app.user.controllers.UserController import UserController
from app.user.entities.UserEntity import UserEntity, UserFromQuery
from app.shared.utils.oauth2 import CustomOauth

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    
)
    
@router.get("/", response_model=UserFromQuery)
def get_user(user = Depends(CustomOauth.get_current_user), userController: UserController = Depends(UserController)):
    return userController.get(user.id)

@router.post("/register")
def create( user: UserEntity, userController: UserController = Depends(UserController)):
    return userController.create(user)
