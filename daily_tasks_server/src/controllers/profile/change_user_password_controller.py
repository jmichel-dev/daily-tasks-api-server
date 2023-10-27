from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.auth.change_password_model import ChangePasswordAuthenticatedRequestModel
from daily_tasks_server.src.models.auth.refresh_token_model import RefreshTokenResponse
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.services.auth.change_password_by_email_service import ChangePasswordByEmailService
from daily_tasks_server.src.services.auth.compare_user_password_service import CompareUserPasswordService
from daily_tasks_server.src.services.jwt.generate_access_refresh_token_service import GenerateAccessRefreshTokenService
from daily_tasks_server.src.services.user.search_user_database_by_email_service import SearchUserDatabaseByEmailService


class ChangeUserPasswordController:

    @staticmethod
    def execute(
            user: UserResponseModel,
            change_password_request: ChangePasswordAuthenticatedRequestModel
    ) -> RefreshTokenResponse:
        db_session = DatabaseSession()

        with db_session.get_session() as session:
            email = user.email

            search_user_service = SearchUserDatabaseByEmailService(session)
            user = search_user_service.execute(email)

            compare_user_password_service = CompareUserPasswordService(session)
            compare_user_password_service.execute(email, change_password_request.old_password)

            change_password_by_email_service = ChangePasswordByEmailService(session)
            change_password_by_email_service.execute(
                email,
                change_password_request.new_password, user.password_salt
            )

            generate_access_refresh_token_service = GenerateAccessRefreshTokenService(session)
            tokens = generate_access_refresh_token_service.execute(email)

            session.commit()

            return tokens

