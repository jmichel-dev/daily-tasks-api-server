from typing import Annotated

from pydantic import EmailStr
from fastapi import APIRouter, status, Depends, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm

from daily_tasks_server.src.controllers.auth.change_password_controller import ChangePasswordController
from daily_tasks_server.src.controllers.auth.change_password_request_controller import ChangePasswordRequestController
from daily_tasks_server.src.controllers.auth.login_user_controller import LoginUserController
from daily_tasks_server.src.controllers.auth.refresh_token_controller import RefreshTokenController
from daily_tasks_server.src.models import UserSignupModel, ChangePasswordModel
from daily_tasks_server.src.models.auth.login_request_response_model import LoginResponseModel, LoginRequestModel
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession

from daily_tasks_server.src.controllers.auth.signup_controller import SignupController
from daily_tasks_server.src.controllers.auth.activate_email_controller import ActivateEmailController
from daily_tasks_server.src.models.auth.refresh_token_model import RefreshTokenResponse, RefreshTokenRequest

router = APIRouter()


@router.post(
    "/token",
    status_code=status.HTTP_200_OK,
    response_model=LoginResponseModel,
    name="Log in user"
)
async def login(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: DatabaseInterface = Depends(DatabaseSession)
) -> LoginResponseModel:
    with db.get_session() as session:
        login_request = LoginRequestModel(email=form_data.username, password=form_data.password)
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


@router.post(
    "/refresh_token",
    name="Refresh Token",
    response_model=RefreshTokenResponse
)
async def refresh_token(
        token_request: RefreshTokenRequest,
        db: DatabaseInterface = Depends(DatabaseSession)
) -> RefreshTokenResponse:
    return await RefreshTokenController().execute(token_request, db)
