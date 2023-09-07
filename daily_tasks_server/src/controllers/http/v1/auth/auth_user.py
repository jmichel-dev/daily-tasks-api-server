from fastapi import APIRouter, status, Depends, BackgroundTasks

from daily_tasks_server.src.models import UserSignupModel
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services import SignupService
from daily_tasks_server.src.services import ActivateUserEmailNotificationService

router = APIRouter()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED
)
async def signup(
        background_task: BackgroundTasks,
        user: UserSignupModel,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    signup_service = SignupService(db.get_session())
    signup_service.execute(user)

    background_task.add_task(ActivateUserEmailNotificationService.notify, user)
