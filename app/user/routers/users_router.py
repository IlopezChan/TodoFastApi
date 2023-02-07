from fastapi import APIRouter, Depends
from app.user.controllers.UserController import UserController
from app.user.entities.UserEntity import UserEntity, UserFromQuery
from app.shared.utils.oauth2 import CustomOauth

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
    
"""
userController injección de dependencia, crea un objeto de tipo UserController y lo guarda en cache para poder ser usado

user = Depends(CustomOauth.get_current_user), injección de dependencia, se obtiene la información del usuario, en base a su jwt

"""
@router.get("/", 
summary="Obtiene informacion del usuario",
description="Endpoint para obtener información del usuario actual",
response_description="Devuelve un objeto con la información del usuario",
response_model=UserFromQuery
)
def get_user(user = Depends(CustomOauth.get_current_user), userController: UserController = Depends(UserController)):
    """
    Devuelve la información del usuario actual en base a su jwt
    - **user** usuario que se obtiene mediante el jwt
    """
    return userController.get(user.id)

@router.post("/register",
summary="Crea un usuario nuevo",
description="Endpoint para crear un usuario nuevo",
response_description="Devuelve un objeto con la información del usuario",
response_model=UserFromQuery,
)
def create( user: UserEntity, userController: UserController = Depends(UserController)):
    """
    Crea un usuario en base a la información proporcionada por el request body
    - **user** Informacion del usuario que se obtiene del requestBody
    """
    return userController.create(user)
