from enum import Enum
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel


class TaskStatus(str, Enum):
    Pending = "PENDING"
    Deleted = "DELETED"
    Cancelled = "CANCELLED"
    Doing = "DOING"
    Finished = "FINISHED"


class TaskPriority(str, Enum):
    Low = "LOW"
    Normal = "NORMAL"
    High = "HIGH"


class TaskRequest(BaseModel):
    title: str
    description: Optional[str]
    status: TaskStatus = TaskStatus.Pending
    priority: TaskPriority = TaskPriority.Normal
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    project_id: str


class TaskResponse(TaskRequest):
    id: str
    created_at: datetime
    updated_at: datetime


class TasksResponse(BaseModel):
    objects: List[TaskResponse] = []


class TaskRequestByProject(BaseModel):
    project_id: str
