from pathlib import Path

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.services import SendEmailService
from daily_tasks_server.src.models import UserResponseModel


class ChangePasswordRequestNotificationService:

    @staticmethod
    def notify(token: str, user: UserResponseModel) -> None:
        html = Path(Config.MAIL_TEMPLATE_REQUEST_PASSWORD_EMAIL).read_text()

        html_message = html.format(
            first_name=user.first_name,
            host=Config.APP_HOST,
            token=token
        )

        SendEmailService.send("Daily Tasks App: Change your password", html_message, user.email)
