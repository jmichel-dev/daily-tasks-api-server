from fastapi import BackgroundTasks

from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.models import UserSignupModel
from daily_tasks_server.src.services import SignupService
from daily_tasks_server.src.services import ActivateUserEmailNotificationService


class SignupController:

    @staticmethod
    def execute(background_task: BackgroundTasks, user: UserSignupModel, db: DatabaseInterface) -> None:
        with db.get_session() as session:
            signup_service = SignupService(session)
            signup_service.execute(user)
            session.commit()

            background_task.add_task(ActivateUserEmailNotificationService.notify, user)
