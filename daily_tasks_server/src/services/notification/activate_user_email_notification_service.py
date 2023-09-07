from daily_tasks_server.src.config import Config
from daily_tasks_server.src.models import UserSignupModel
from daily_tasks_server.src.services import JWTService


class ActivateUserEmailNotification:

    @staticmethod
    async def notify(user: UserSignupModel) -> None:
        payload = {"email": user.email}
        expiration = Config.JWT_ACTIVATE_EMAIL_TOKEN_EXPIRATION

        token = JWTService.generate(payload, expiration)
