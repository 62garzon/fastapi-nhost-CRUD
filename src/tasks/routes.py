from fastapi import APIRouter, Depends, status
from typing import List
from .schemas import Task, TaskCreateModel, TaskUpdateModel
from .service import TaskService
from src.auth.dependencies import AccessTokenBearer
from src.errors import TaskNotFound

task_router = APIRouter()
task_service = TaskService()
access_token_bearer = AccessTokenBearer()


@task_router.get("/", response_model=List[Task])
async def get_all_task(auth_details: dict = Depends(access_token_bearer)):
    tasks = await task_service.get_all_tasks(auth_details)
    return tasks


@task_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Task)
async def create_a_task(task_data: TaskCreateModel, auth_details: dict = Depends(access_token_bearer)) -> dict:
    new_task = await task_service.create_task(task_data, auth_details)
    return new_task


@task_router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int, auth_details: dict = Depends(access_token_bearer)):
    task = await task_service.get_task(task_id, auth_details)
    if task:
        return task
    else:
        raise TaskNotFound()


@task_router.put("/{task_id}", response_model=Task)
async def update_task(task_id, task_data: TaskUpdateModel, auth_details: dict = Depends(access_token_bearer)):
    task = await task_service.update_task(task_id, task_data, auth_details)
    if task:
        return task
    else:
        raise TaskNotFound()


@task_router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, auth_details: dict = Depends(access_token_bearer)):
    task_to_delete = await task_service.delete_task(task_id, auth_details)
    if not task_to_delete:
        raise TaskNotFound()

