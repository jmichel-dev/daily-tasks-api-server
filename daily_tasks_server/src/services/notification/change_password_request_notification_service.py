from pathlib import Path

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.services import SendEmailService


class ChangePasswordRequestNotificationService:

    @staticmethod
    def notify(token: str, email: str) -> None:
        html = Path(Config.MAIL_TEMPLATE_REQUEST_PASSWORD_EMAIL).read_text()

        html_message = html.format(
            email=email,
            host=Config.APP_HOST,
            token=token
        )

        SendEmailService.send("Daily Tasks App: Please, confirm your email", html_message, email)