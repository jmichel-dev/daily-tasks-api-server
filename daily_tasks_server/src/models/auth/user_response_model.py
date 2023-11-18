from datetime import datetime
from pydantic import BaseModel


class UserResponseModel(BaseModel):

    uid: str
    first_name: str
    last_name: str
    email: str
    active_email: bool
    avatar_url: str
    enable: bool
    created_at: datetime
    updated_at: datetime


class UserDatabaseModel(UserResponseModel):
    password_salt: bytes
    password: str
