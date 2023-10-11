from fastapi import HTTPException, status
from jose import JWTError

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.models.auth.refresh_token_model import RefreshTokenResponse
from daily_tasks_server.src.services import JWTService
from daily_tasks_server.src.services.user.search_user_by_email import SearchUserByEmail


class RefreshTokenController:

    @staticmethod
    async def execute(token: str, db: DatabaseInterface) -> RefreshTokenResponse:
        try:
            with db.get_session() as session:
                payload = JWTService.verify(token)
                email = payload["payload"]["email"]

                search_user_by_email_service = SearchUserByEmail(session)
                _ = search_user_by_email_service.execute(email)

                token_payload = {
                    "email": email
                }

                refresh_token = JWTService.generate(
                    payload=token_payload,
                    expiration=Config.JWT_REFRESH_TOKEN_EXPIRATION
                )

                access_token = JWTService.generate(
                    payload=token_payload,
                    expiration=Config.JWT_ACCESS_TOKEN_EXPIRATION
                )

                return RefreshTokenResponse(
                    refresh_token=refresh_token,
                    access_token=access_token
                )
        except JWTError:
            raise HTTPException(
                detail="Refresh token is not valid",
                status_code=status.HTTP_401_UNAUTHORIZED
            )


