from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.services import JWTService
from daily_tasks_server.src.services import ConfirmEmailService


class ActivateEmailController:

    @staticmethod
    def execute(token: str, db: DatabaseInterface) -> None:
        payload = JWTService.verify(token)

        user = payload["payload"]["email"]

        with db.get_session() as session:
            confirm_email_service = ConfirmEmailService(session)
            confirm_email_service.execute(user)
            session.commit()
