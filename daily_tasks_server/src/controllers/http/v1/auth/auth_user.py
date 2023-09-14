from pydantic import EmailStr
from psycopg2.extensions import connection
from fastapi import APIRouter, status, Depends, BackgroundTasks

from daily_tasks_server.src.models import UserSignupModel, ChangePasswordModel
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services import SignupService
from daily_tasks_server.src.services import ActivateUserEmailNotificationService
from daily_tasks_server.src.services import JWTService
from daily_tasks_server.src.services import ConfirmEmailService
from daily_tasks_server.src.services import RequestChangePasswordService
from daily_tasks_server.src.services import DisableTokenService
from daily_tasks_server.src.services import VerityJWTTokenDatabaseService
from daily_tasks_server.src.services import ChangePasswordByEmailService

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
    "/password",
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


@router.put(
    "/password",
    status_code=status.HTTP_200_OK,
    name="Change password"
)
def change_password(
        password_request: ChangePasswordModel,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    with db.get_session() as session:
        session: connection = session
        payload = JWTService.verify(password_request.token)
        email = payload["payload"]["email"]

        verify_token_service = VerityJWTTokenDatabaseService(session)
        verify_token_service.execute(password_request.token)

        disable_token_service = DisableTokenService(session)
        disable_token_service.execute(password_request.token)

        change_password_service = ChangePasswordByEmailService(session)
        change_password_service.execute(email, password_request.new_password)

        session.commit()
