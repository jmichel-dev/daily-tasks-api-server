import json

from pydantic import EmailStr
from fastapi import APIRouter, status, Depends, BackgroundTasks

from daily_tasks_server.src.models import UserSignupModel
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services import SignupService
from daily_tasks_server.src.services import ActivateUserEmailNotificationService
from daily_tasks_server.src.services import JWTService
from daily_tasks_server.src.services import ConfirmEmailService
from daily_tasks_server.src.services import RequestChangePasswordService

router = APIRouter()


@router.post(
    '/signup/',
    status_code=status.HTTP_201_CREATED,
    name="Signup user"
)
async def signup(
        background_task: BackgroundTasks,
        user: UserSignupModel,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    signup_service = SignupService(db.get_session())
    signup_service.execute(user)

    background_task.add_task(ActivateUserEmailNotificationService.notify, user)


@router.post(
    "/activate/{token}",
    status_code=status.HTTP_200_OK,
    name="Activate user email"
)
async def activate(
        token: str,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    payload = JWTService.verify(token)

    user = payload["payload"]["email"]
    confirm_email_service = ConfirmEmailService(db_session=db.get_session())
    confirm_email_service.execute(user)


@router.post(
    "/change_password",
    status_code=status.HTTP_200_OK,
    name="Request change password"
)
def change_password_request(
        background_task: BackgroundTasks,
        email: EmailStr,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    change_password_request_service = RequestChangePasswordService(db.get_session())

    change_password_request_service.execute(email, background_task)
