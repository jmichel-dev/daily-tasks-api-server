from pydantic import BaseModel


class RefreshTokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshTokenRequest(RefreshTokenResponse):
    ...
