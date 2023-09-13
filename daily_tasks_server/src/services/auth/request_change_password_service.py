from fastapi import BackgroundTasks

from daily_tasks_server.src.services import GenerateAndSaveTokenService
from daily_tasks_server.src.services import ChangePasswordRequestNotificationService


class RequestChangePasswordService:

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def execute(self, email: str, background_task: BackgroundTasks) -> None:
        generate_token_service = GenerateAndSaveTokenService(self.db_session)
        token = generate_token_service.execute(email)

        background_task.add_task(ChangePasswordRequestNotificationService.notify, token, email)
