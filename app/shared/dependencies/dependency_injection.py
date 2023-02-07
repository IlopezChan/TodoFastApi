from app.auth.services.AuthServiceImpl import AuthServiceImpl
from app.task.controllers.TaskCrontroller import TaskCrontroller
from app.task.interactors.TaskInteractor import TaskInteractor
from app.task.repositories.TaskRepository import TaskRepository
from app.task.services.TaskServiceImpl import TaskServiceImpl
from app.user.repositories.UserRepository import UserRepository
from config.database_config import (
    get_db_connection,
)


user = AuthServiceImpl(UserRepository(get_db_connection)).get_current_user

def task_dependency():
    return TaskCrontroller(TaskInteractor(TaskServiceImpl(TaskRepository(get_db_connection))))
