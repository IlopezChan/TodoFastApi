import uvicorn
from fastapi import FastAPI
from app.user.routers import users_router
from app.auth.routers import auth_router
from app.task.routers import tasks_router
from config.env_variables import ENV, HOST, APP_PORT
from app.doc.documentation import tags_metadata

app = FastAPI(openapi_tags=tags_metadata)
app.include_router(users_router.router)
app.include_router(auth_router.router)
app.include_router(tasks_router.router)

if __name__ == "__main__":
    hot_reload = True if ENV=="dev" else False
    uvicorn.run("app.main:app", host=HOST, port=APP_PORT, log_level="info", reload=hot_reload)
