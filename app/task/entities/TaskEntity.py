from pydantic import BaseModel, validator, ValidationError
from typing import Optional, List
from datetime import date
import enum

class TaskEntity(BaseModel):
    Nombre: str
    Descripcion: str

class TaskCreated(TaskEntity):
    id: int
    Estatus: Optional[enum.Enum]
    FechaAlta: Optional[date]
    FechaBaja: Optional[date]
    user_id: int

    class Config:
        orm_mode=True

class TaskUpdate(BaseModel):
    Nombre: Optional[str]
    Descripcion: Optional[str]
    Estatus: Optional[str]

    @validator('Estatus')
    def check_estatus(cls, estatus):
        if ((estatus != 'Completado' ) and (estatus != 'Activo')):
            raise ValueError('Estatus solo puede ser Activo o Completado')
        return estatus



class TaskResponse(BaseModel):
    id: int
    Nombre: str
    Descripcion: str
    Estatus: Optional[enum.Enum]
    FechaAlta: Optional[date]
    FechaBaja: Optional[date]

    class Config:
        orm_mode=True

class TaskDelete(BaseModel):
    msg: str
    task: TaskResponse

    class Config:
        orm_mode=True

class TaskList(BaseModel):
    __root__: List[TaskResponse]