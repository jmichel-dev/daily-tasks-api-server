from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class ProjectResponse(BaseModel):
    id: str
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    owner: str


class ProjectRequest(BaseModel):
    title: str
    description: Optional[str]
