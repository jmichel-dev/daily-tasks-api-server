from datetime import datetime

from jose import jwt
from fastapi import HTTPException, status

from daily_tasks_server.src.config import Config


class JWTService:

    @staticmethod
    def generate(payload: dict, expiration: datetime) -> str:
        claims = {
            "payload": payload,
            "exp": expiration
        }
        return jwt.encode(
            claims=claims,
            key=Config.JWT_SECRET,
            algorithm=Config.JWT_ALGORITHM
        )

    @staticmethod
    def verify(token: str) -> dict:
        try:
            return jwt.decode(
                token=token,
                key=Config.JWT_SECRET,
                algorithms=[Config.JWT_ALGORITHM]
            )
        except (jwt.JWTError, jwt.ExpiredSignatureError):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token invalid"
            )
