from fastapi import Depends
from sqlalchemy import update
from sqlalchemy.orm import Session
from typing import List
from app.shared.base.BaseRepository import BaseRepository
from app.task.models.TaskModel import Task
from datetime import datetime
from config.database_config import Engine


class TaskRepository(BaseRepository):
    def __init__(self, eng:Engine):
        self.eng = eng

    def get_all(self) -> List:
        return super().get_all()
    
    def get_all_by_user(self, user) -> List:
        with Session(self.eng) as db:
            tasks = db.query(Task).filter(Task.user_id == user.id).all()
        return tasks
    
    def get_by_id(self, id: int, user):
        with Session(self.eng) as db:
            task = db.query(Task).filter(Task.id == id, Task.user_id==user.id ).first()
            return task
    
    def create(self, Entity):
        with Session(self.eng) as db:
            db.add(Entity)
            db.commit()
            db.refresh(Entity)
            return Entity
    
    def update(self, user, id, task):
        with Session(self.eng) as db:
            _task = db.query(Task).filter(Task.id==id, Task.user_id==user.id).first() 
            _task.Nombre = task.Nombre
            _task.Descripcion = task.Descripcion
            _task.Estatus = task.Estatus
            _task.FechaBaja=datetime.today().strftime('%Y-%m-%d')
            db.commit()
            db.refresh(_task)
            return _task
           
    def delete(self, id: int, user):
        with Session(self.eng) as db:
            task = db.query(Task).filter(Task.id==id, Task.user_id==user.id).first()
            db.delete(task)
            db.commit()
            return task
            
    

    
    