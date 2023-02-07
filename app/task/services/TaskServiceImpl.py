from fastapi import Depends, HTTPException, status
from app.shared.base.BaseService import BaseService
from app.task.models.TaskModel import Task
from app.task.entities.TaskEntity import TaskEntity, TaskDelete, TaskCreated
from app.task.repositories.TaskRepository import TaskRepository
from datetime import datetime

class TaskServiceImpl(BaseService):
        
    def create_task(self, task: TaskEntity, user, taskRepository: TaskRepository):
        task: Task = Task(
            Nombre = task.Nombre,
            Descripcion=task.Descripcion,
            FechaAlta=datetime.today().strftime('%Y-%m-%d'),
            user_id=user.id
        )
        return taskRepository.create(task)
    
    def get_all_by_user(self, user, repository:TaskRepository):
        return repository.get_all_by_user(user)
    
    def get_task_by_user(self, id:int, user, repository):
        return self.check_task(user=user, task_id=id, repository=repository)
        
    def update(self, user, task_id: int, task, repository:TaskRepository):
        self.check_task(user, task_id, repository)
        return repository.update(user, task_id, task)
    
    def delete(self, task_id: int, user, repository: TaskRepository):
        self.check_task(user, task_id, repository)
        task_delete = TaskCreated.from_orm(repository.delete(task_id, user))
        return TaskDelete(msg="Tarea Eliminada",task=task_delete)

    @staticmethod
    def check_task(user, task_id, repository):
        task = repository.get_by_id(task_id, user)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea No Encontrada")
        return task


    