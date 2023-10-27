from fastapi import HTTPException, status

from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.models.auth.change_password_model import ChangePasswordModel
from daily_tasks_server.src.services import JWTService, VerityJWTTokenDatabaseService, DisableTokenService
from daily_tasks_server.src.services.auth.change_password_by_email_service import ChangePasswordByEmailService
from daily_tasks_server.src.services.auth.compare_user_password_service import CompareUserPasswordService
from daily_tasks_server.src.services.user.search_user_database_by_email_service import SearchUserDatabaseByEmailService


class ChangePasswordController:

    @staticmethod
    def execute(password_request: ChangePasswordModel, db: DatabaseInterface) -> None:
        with db.get_session() as session:
            payload = JWTService.verify(password_request.token)
            email = payload["payload"]["email"]

            search_user_database_by_email_service = SearchUserDatabaseByEmailService(session)
            user = search_user_database_by_email_service.execute(email)

            verify_token_service = VerityJWTTokenDatabaseService(session)
            verify_token_service.execute(password_request.token)

            disable_token_service = DisableTokenService(session)
            disable_token_service.execute(password_request.token)

            change_password_service = ChangePasswordByEmailService(session)
            change_password_service.execute(email, password_request.new_password, user.password_salt)

            session.commit()
