from fastapi import Depends
from app.shared.base.BaseInteractor import BaseInteractor
from app.task.entities.TaskEntity import TaskEntity
from app.task.services.TaskServiceImpl import TaskServiceImpl


class TaskInteractor(BaseInteractor):

    def __init__(self, taskService:TaskServiceImpl = Depends()):
        self.taskService = taskService
    

    def create_task(self, task:TaskEntity, user, taskRepository):
        return self.taskService.create_task(task, user, taskRepository)
    
    def create(requestBody, repository):
        return super().create(repository)
    
    def get_all_by_user(self, user, repository):
        return self.taskService.get_all_by_user(user, repository)
    
    def get_task_by_user(self, id:int, user, repository):
        return self.taskService.get_task_by_user(id, user, repository)
    
    def update(self, user, id: int, task, repository):
        return self.taskService.update(user, id,task, repository)

    def delete(self, id: int, user, repository):
        return self.taskService.delete(id, user, repository)
    
        