from pathlib import Path

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.models import UserSignupModel
from daily_tasks_server.src.services import JWTService
from daily_tasks_server.src.services import SendEmailService


class ActivateUserEmailNotificationService:

    @staticmethod
    def notify(user: UserSignupModel) -> None:
        payload = {"email": user.email}
        expiration = Config.JWT_ACTIVATE_EMAIL_TOKEN_EXPIRATION

        token = JWTService.generate(payload, expiration)
        html = Path(Config.MAIL_TEMPLATE_ACTIVATE_USER_EMAIL).read_text()

        html_message = html.format(
            first_name=user.first_name,
            host=Config.APP_HOST,
            token=token
        )

        SendEmailService.send("Daily Tasks App: Please, confirm your email", html_message, user.email)
