import datetime
import enum
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Enum, Date
from config.database_config import Base


class EstatusEnum(enum.Enum):
    Activo= 'A'
    Completado = 'C'
    
class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    Descripcion = Column(String(255))
    Estatus = Column(Enum(EstatusEnum),  default=EstatusEnum.Activo)
    FechaAlta = Column(Date(), nullable=True)
    FechaBaja = Column(Date(), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

    def __init__(self, Nombre, Descripcion, FechaAlta, user_id):
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.FechaAlta = FechaAlta
        self.user_id = user_id
    

    def __repr__(self):

        return f'tasks(id: {self.id}, Nombre: {self.Nombre}, Descripcion: {self.Descripcion}, Estatus: {self.Estatus}, Fecha Alta: {self.FechaAlta}, Fecha Baja: {self.FechaBaja}, Usuario: {self.user_id} )'

    

