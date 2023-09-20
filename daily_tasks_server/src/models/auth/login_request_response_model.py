from pydantic import BaseModel, EmailStr

from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel


class LoginRequestModel(BaseModel):
    email: EmailStr
    password: str


class LoginResponseModel(BaseModel):
    user: UserResponseModel
    access_token: str
    refresh_token: str
