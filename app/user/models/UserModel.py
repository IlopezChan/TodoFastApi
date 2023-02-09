import enum
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Date, DateTime, Enum
from config.database_config import Base

class EstatusEnum(enum.Enum):
    Activo= 'A'
    Inactivo = 'I'
    Bloqueado = 'B'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(255))
    UserName = Column(String(100))
    Email = Column(String(255))
    Password = Column(String(250), nullable=True)
    Estatus = Column(Enum(EstatusEnum), default=EstatusEnum.Activo)
    FechaAlta = Column(Date(), nullable=True)

    tasks = relationship("Task", back_populates="user")

   
    def __init__(self, Nombre, UserName, Email, Password, FechaAlta):
        self.Nombre = Nombre
        self.UserName = UserName
        self.Email = Email
        self.Password = Password
        self.FechaAlta = FechaAlta
        

    def __repr__(self):
        return f'users({self.id}, {self.Email})'

   

