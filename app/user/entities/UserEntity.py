from pydantic import BaseModel
from typing import Optional, List
from datetime import date
import enum

class UserEntity(BaseModel):
    Nombre: str
    UserName: str
    Email: str
    Password: str

    class Config:
        orm_mode = True

class UserIn(BaseModel):
    Email:  Optional[str]
    Password: Optional[str]
    
    class Config:
        orm_mode = True

class UserLogIn(UserEntity):
    Estatus: Optional[enum.Enum]
    FechaAlta: Optional[date]

    class Config:
        orm_mode = True
        
class UserFromQuery(BaseModel):
    id: int
    Nombre: str
    UserName: str
    Email: str
    Estatus: Optional[enum.Enum]
    FechaAlta: Optional[date]

    class Config:
        orm_mode = True

class UserList(BaseModel):
    __root__: List[UserFromQuery]


