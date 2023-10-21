from fastapi import BackgroundTasks

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.services import GenerateAndSaveTokenService
from daily_tasks_server.src.services.notification.change_password_request_notification_service import \
    ChangePasswordRequestNotificationService
from daily_tasks_server.src.services.user.search_user_by_email import SearchUserByEmail


class ChangePasswordRequestController:

    @staticmethod
    def execute(email: str, background_task: BackgroundTasks, db: DatabaseInterface) -> None:
        with db.get_session() as session:
            search_user_by_email_service = SearchUserByEmail(session)
            generate_token_service = GenerateAndSaveTokenService(session)

            payload = {
                "email": email
            }
            expiration_time = Config.JWT_ACTIVATE_EMAIL_TOKEN_EXPIRATION
            token = generate_token_service.execute(payload, expiration_time)
            user = search_user_by_email_service.execute(email)
            session.commit()

            background_task.add_task(ChangePasswordRequestNotificationService.notify, token, user)
