from pydantic import BaseModel, EmailStr, Field

from daily_tasks_server.src.config import Config


class UserSignupModel(BaseModel):
    first_name: str = Field(title="First Name", description="Your first name", min_length=2, max_length=80)
    last_name: str = Field(title="Last name", description="Your last name", min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(title="Password", description="Your password", min_length=Config.PASSWORD_MIN_LENGTH)
