from pydantic import BaseModel, model_validator


class ChangePasswordModel(BaseModel):

    token: str
    new_password: str
    retype_password: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'ChangePasswordModel':
        pw1 = self.new_password
        pw2 = self.retype_password
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self


class ChangePasswordAuthenticatedRequestModel(ChangePasswordModel):
    old_password: str
    new_password: str
    retype_password: str

    @model_validator(mode='after')
    def check_passwords_match(self) -> 'ChangePasswordAuthenticatedRequestModel':
        pw1 = self.new_password
        pw2 = self.retype_password
        if pw1 is not None and pw2 is not None and pw1 != pw2:
            raise ValueError('passwords do not match')
        return self
