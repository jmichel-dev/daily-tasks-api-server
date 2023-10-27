from fastapi import HTTPException, status
from jose import JWTError

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.models.auth.refresh_token_model import RefreshTokenResponse, RefreshTokenRequest
from daily_tasks_server.src.services import JWTService, GenerateAndSaveTokenService, DisableTokenService, \
    VerityJWTTokenDatabaseService
from daily_tasks_server.src.services.jwt.generate_access_refresh_token_service import GenerateAccessRefreshTokenService
from daily_tasks_server.src.services.user.search_user_by_email import SearchUserByEmail


class RefreshTokenController:

    @staticmethod
    async def execute(token_request: RefreshTokenRequest, db: DatabaseInterface) -> RefreshTokenResponse:
        try:
            with db.get_session() as session:
                payload = JWTService.verify(token_request.refresh_token)
                email = payload["payload"]["email"]
                
                verify_token_validate_service = VerityJWTTokenDatabaseService(session)
                verify_token_validate_service.execute(token_request.refresh_token)

                search_user_by_email_service = SearchUserByEmail(session)
                _ = search_user_by_email_service.execute(email)

                disable_token_service = DisableTokenService(session)
                disable_token_service.execute(token_request.refresh_token)
                disable_token_service.execute(token_request.access_token)

                generate_access_refresh_token_service = GenerateAccessRefreshTokenService(session)
                tokens_response = generate_access_refresh_token_service.execute(email)

                session.commit()

                return tokens_response
        except JWTError:
            raise HTTPException(
                detail="Refresh token is not valid",
                status_code=status.HTTP_401_UNAUTHORIZED
            )


