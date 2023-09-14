from pydantic import BaseModel


class ChangePasswordModel(BaseModel):

    token: str
    old_password: str
    new_password: str
