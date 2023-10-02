from typing import Annotated

from fastapi import APIRouter, Depends

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.controllers.task.create_task_controller import CreateTaskController
from daily_tasks_server.src.controllers.task.list_all_tasks_controller import ListAllTasksController
from daily_tasks_server.src.controllers.task.list_task_by_id_controller import ListTaskByIdController
from daily_tasks_server.src.controllers.task.update_task_controller import UpdateTaskController
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.task.task_model import TasksResponse, TaskResponse, TaskRequest

router = APIRouter()


@router.get(
    "/{project_id}/task",
    response_model=TasksResponse,
)
def list_tasks(
        project_id: str,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> TasksResponse:
    return ListAllTasksController.execute(current_user, project_id)


@router.post(
    "/{project_id}/task",
    response_model=TaskResponse
)
def create_task(
        project_id: str,
        task_request: TaskRequest,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> TaskResponse:
    return CreateTaskController.execute(project_id, current_user, task_request)


@router.get(
    "/{project_id}/task/{task_id}",
    response_model=TaskResponse
)
def list_task(
        project_id: str,
        task_id: str,
        _: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> TaskResponse:
    return ListTaskByIdController.execute(project_id, task_id)


@router.put(
    "/{project_id}/task/{task_id}",
    response_model=TaskResponse
)
def update_task(
        project_id: str,
        task_id: str,
        task_request: TaskRequest,
        _: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> TaskResponse:
    return UpdateTaskController.execute(project_id, task_id, task_request)
