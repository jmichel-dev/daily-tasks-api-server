from psycopg2.extensions import connection

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.models.auth.refresh_token_model import RefreshTokenResponse
from daily_tasks_server.src.services import GenerateAndSaveTokenService


class GenerateAccessRefreshTokenService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str) -> RefreshTokenResponse:
        generate_and_save_token_service = GenerateAndSaveTokenService(self.db_session)

        token_payload = {
            "email": email
        }

        refresh_token = generate_and_save_token_service.execute(
            token_payload,
            Config.JWT_REFRESH_TOKEN_EXPIRATION
        )

        access_token = generate_and_save_token_service.execute(
            token_payload,
            Config.JWT_ACCESS_TOKEN_EXPIRATION
        )

        return RefreshTokenResponse(
            refresh_token=refresh_token,
            access_token=access_token
        )
