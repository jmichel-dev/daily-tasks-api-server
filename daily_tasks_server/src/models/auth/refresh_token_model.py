from pydantic import BaseModel


class RefreshTokenRequest(BaseModel):
    token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    refresh_token: str
