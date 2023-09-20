from pydantic import EmailStr
from fastapi import APIRouter, status, Depends, BackgroundTasks

from daily_tasks_server.src.controllers.auth.change_password_controller import ChangePasswordController
from daily_tasks_server.src.controllers.auth.change_password_request_controller import ChangePasswordRequestController
from daily_tasks_server.src.controllers.auth.login_user_controller import LoginUserController
from daily_tasks_server.src.models import UserSignupModel, ChangePasswordModel
from daily_tasks_server.src.models.auth.login_request_response_model import LoginResponseModel, LoginRequestModel
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession

from daily_tasks_server.src.controllers.auth.signup_controller import SignupController
from daily_tasks_server.src.controllers.auth.activate_email_controller import ActivateEmailController


router = APIRouter()


@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseModel,
    name="Log in user"
)
async def login(
        login_request: LoginRequestModel,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> LoginResponseModel:
    with db.get_session() as session:
        return LoginUserController.execute(login_request, session)


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
    SignupController.execute(background_task, user, db)


@router.post(
    "/activate/{token}",
    status_code=status.HTTP_200_OK,
    name="Activate user email"
)
async def activate(
        token: str,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    ActivateEmailController.execute(token, db)


@router.post(
    "/password",
    status_code=status.HTTP_200_OK,
    name="Change password request"
)
def change_password_request(
        background_task: BackgroundTasks,
        email: EmailStr,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    ChangePasswordRequestController.execute(email, background_task, db)


@router.put(
    "/password",
    status_code=status.HTTP_200_OK,
    name="Change password"
)
def change_password(
        password_request: ChangePasswordModel,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> None:
    ChangePasswordController.execute(password_request, db)
