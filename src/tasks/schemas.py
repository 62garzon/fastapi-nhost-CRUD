from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    id: int
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class TaskCreateModel(BaseModel):
    title: str
    description: Optional[str] = None


class TaskUpdateModel(BaseModel):
    title: str
    description: str
    is_completed: bool
