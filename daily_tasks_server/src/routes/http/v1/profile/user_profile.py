from typing import Annotated

from fastapi import APIRouter, status, Depends

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.controllers.profile.change_user_password_controller import ChangeUserPasswordController
from daily_tasks_server.src.models.auth.change_password_model import ChangePasswordAuthenticatedRequestModel
from daily_tasks_server.src.models.auth.refresh_token_model import RefreshTokenResponse
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel

router = APIRouter()


@router.get(
    "/me",
    status_code=status.HTTP_200_OK
)
async def me(current_user: Annotated[UserResponseModel, Depends(get_current_active_user)]) -> UserResponseModel:
    return current_user


@router.post(
    "/change_password",
    response_model=RefreshTokenResponse
)
async def change_password(
        change_password_request: ChangePasswordAuthenticatedRequestModel,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)]
) -> RefreshTokenResponse:
    return ChangeUserPasswordController.execute(current_user, change_password_request)
