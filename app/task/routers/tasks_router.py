from fastapi import APIRouter, Depends
from app.task.controllers.TaskCrontroller import TaskCrontroller
from app.task.entities.TaskEntity import TaskEntity, TaskCreated, TaskList, TaskUpdate, TaskResponse, TaskDelete
from app.shared.utils.oauth2 import CustomOauth

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", 
summary="Devuelve todas las tareas del usuario",
description="Endpoint para consultar todas las tareas del usuario",
response_description="Devuelve una lista de todas las tareas del usuario",
response_model=TaskList)
def get_all_tasks(user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    return taskController.get_all_by_user(user)

@router.post("/", 
summary="Crea una tarea",
description="Endpoint para crear tareas por usuario",
response_description="Devuelve la tarea creada",
response_model=TaskCreated)
def create_task(task:TaskEntity, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    """
    Función para crear una tarea, obtiene la información del usuario por medio de su jwt
    acepta el parametro task
    - **task** requestBody que representa la tarea a crear
    """
    return taskController.create_task(task=task, user=user)

@router.get("/{task_id}",
summary="Obtiene una tarea",
description="Endpoint para obtener una tarea en especifico por usuario",
response_description="Devuelve la tarea especificada",
response_model=TaskResponse
)
def get_task(task_id:int, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    """
    Función que devuelve una tarea, realiza la busqueda por su id
    - **task_id** Id de la tarea especifica a obtener
    """
    task = taskController.get(task_id, user)
    print(task)
    return task

@router.put("/{task_id}",
summary="Actualiza una tarea",
description="Endpoint para actualizar una tarea en especifico por usuario",
response_description="Devuelve la tarea actualizada",
response_model=TaskResponse
)
def update_task(task_id:int, task: TaskUpdate, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    """
    Función que actualiza una tarea, realiza la busqueda por su id
    
    - **task_id** Id de la tarea especifica a actualizar
    """
    return taskController.update(user, task_id, task)

@router.delete("/{task_id}",
summary="Elimina una tarea",
description="Endpoint para eliminar una tarea en especifico por usuario",
response_description="Devuelve la tarea eliminada",
response_model=TaskDelete)
def delete_task(task_id:int, user = Depends(CustomOauth.get_current_user), taskController:TaskCrontroller = Depends()):
    """
    Función que elimina una tarea, realiza la busqueda por su id
    - **task_id** Id de la tarea especifica a eliminar
    """
    return taskController.delete(task_id, user)

    
    


