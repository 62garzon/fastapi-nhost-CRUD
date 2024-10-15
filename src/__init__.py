from fastapi import FastAPI
from src.tasks.routes import task_router
from src.auth.routes import auth_router
from .errors import register_all_errors

version = "v1"

description = """
A REST API for a Task.

This REST API is able to;
- Create Read Update and Delete task
"""

version_prefix = f"/api/{version}"

app = FastAPI(
    title="Task CRUD",
    description=description,
    version=version
)

register_all_errors(app)

app.include_router(task_router, prefix=f"{version_prefix}/tasks", tags=["tasks"])
app.include_router(auth_router, prefix=f"{version_prefix}/auth", tags= ["auth"])
