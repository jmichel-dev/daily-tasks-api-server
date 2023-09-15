from datetime import datetime
from pydantic import BaseModel


class UserResponseModel(BaseModel):
    uid: str
    first_name: str
    last_name: str
    email: str
    active_email: bool
    enable: bool
    created_at: datetime
    updated_at: datetime
