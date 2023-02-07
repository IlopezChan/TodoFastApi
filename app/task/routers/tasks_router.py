from fastapi import APIRouter, Depends
from app.task.controllers.TaskCrontroller import TaskCrontroller
from app.task.entities.TaskEntity import TaskEntity, TaskCreated, TaskList, TaskUpdate
from app.shared.utils.oauth2 import CustomOauth

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=TaskList)
def get_all_tasks(user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    return taskController.get_all_by_user(user)

@router.post("/", response_model=TaskCreated)
def create_task(task:TaskEntity, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    return taskController.create_task(task=task, user=user)

@router.get("/{task_id}")
def get_task(task_id:int, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    return taskController.get(task_id, user)

@router.put("/{task_id}")
def update_task(task_id:int, task: TaskUpdate, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    return taskController.update(user, task_id, task)

@router.delete("/{task_id}")
def delete_task(task_id:int, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    return taskController.delete(task_id, user)

    
    


