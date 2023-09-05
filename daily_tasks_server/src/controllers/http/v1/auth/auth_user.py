from fastapi import APIRouter, status, Depends

from daily_tasks_server.src.models import UserSignupModel
from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database import DatabaseSession

router = APIRouter()


@router.post(
    '',
    status_code=status.HTTP_201_CREATED
)
async def signup(
        user: UserSignupModel,
        session: DatabaseInterface = Depends(DatabaseSession)
) -> dict:
    return {"msg": "Hello, World"}
