from typing import Optional
from datetime import datetime

from pydantic import BaseModel

from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel


class ProjectResponse:
    id: str
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    owner: UserResponseModel


class ProjectRequest:
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    owner_id: str
