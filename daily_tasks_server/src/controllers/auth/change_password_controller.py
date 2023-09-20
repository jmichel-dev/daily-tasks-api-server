from fastapi import HTTPException, status

from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.models.auth.change_password_model import ChangePasswordModel
from daily_tasks_server.src.services import JWTService, VerityJWTTokenDatabaseService, DisableTokenService
from daily_tasks_server.src.services.auth.change_password_by_email_service import ChangePasswordByEmailService
from daily_tasks_server.src.services.auth.compare_user_password_service import CompareUserPasswordService


class ChangePasswordController:

    @staticmethod
    def execute(password_request: ChangePasswordModel, db: DatabaseInterface) -> None:
        with db.get_session() as session:
            payload = JWTService.verify(password_request.token)
            email = payload["payload"]["email"]

            compare_user_password_service = CompareUserPasswordService(session)
            valid_password = compare_user_password_service.execute(email, password_request.old_password)

            if not valid_password:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email/password invalid"
                )

            verify_token_service = VerityJWTTokenDatabaseService(session)
            verify_token_service.execute(password_request.token)

            disable_token_service = DisableTokenService(session)
            disable_token_service.execute(password_request.token)

            change_password_service = ChangePasswordByEmailService(session)
            change_password_service.execute(email, password_request.new_password)

            session.commit()
