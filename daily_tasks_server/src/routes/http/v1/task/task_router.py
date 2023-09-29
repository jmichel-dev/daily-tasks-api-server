from typing import Annotated

from fastapi import APIRouter, Depends

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.controllers.task.list_all_tasks_controller import ListAllTasksController
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.task.task_model import TasksResponse

router = APIRouter()


@router.get(
    "/{project_id}/tasks",
    response_model=TasksResponse,
)
def list_tasks(
        project_id: str,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> TasksResponse:
    return ListAllTasksController.execute(current_user, project_id)
