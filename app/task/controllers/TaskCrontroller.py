from fastapi import Depends
from app.task.interactors.TaskInteractor import TaskInteractor
from app.task.entities.TaskEntity import TaskEntity
from config.database_config import Engine
from app.task.repositories.TaskRepository import TaskRepository
from app.shared.base.BaseController import BaseController

class TaskCrontroller(BaseController):
    def __init__(self, taskInteractor: TaskInteractor = Depends(TaskInteractor)):
        self.taskRepository = TaskRepository(eng=Engine)
        self.taskInteractor = taskInteractor

    def get_all_by_user(self, user):
        return self.taskInteractor.get_all_by_user(user, self.taskRepository)

    def create_task(self, task:TaskEntity, user):
        return self.taskInteractor.create_task(task, user, self.taskRepository)
    
    def get(self, id:int, user):
        return self.taskInteractor.get_task_by_user(id, user, self.taskRepository)
    
    def update(self, user, id: int, task):
        return self.taskInteractor.update(user, id, task, self.taskRepository)

    def delete(self,  id: int, user):
        return self.taskInteractor.delete(id, user, self.taskRepository)