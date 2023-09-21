from typing import Annotated

from fastapi import APIRouter, status, Depends

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel

router = APIRouter()


@router.get(
    "/me",
    status_code=status.HTTP_200_OK
)
async def me(current_user: Annotated[UserResponseModel, Depends(get_current_active_user)]) -> UserResponseModel:
    return current_user
