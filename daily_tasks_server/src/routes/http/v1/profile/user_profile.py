from fastapi import APIRouter, status

from daily_tasks_server.src.config.authentication import oauth2_scheme


router = APIRouter()


@router.get(
    "/me",
    status_code=status.HTTP_200_OK
)
async def me() -> None:
    ...
