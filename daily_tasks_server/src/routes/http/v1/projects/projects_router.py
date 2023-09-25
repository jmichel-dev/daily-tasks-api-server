from typing import Annotated

from psycopg2.extensions import connection
from fastapi import APIRouter, status, Depends

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.config.database import DatabaseInterface, DatabaseSession
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.projects.project_models import ProjectResponse, ProjectRequest
from daily_tasks_server.src.controllers.project.create_project_controller import CreateProjectController


router = APIRouter()


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    name="Create project"
)
def create_project(
        project: ProjectRequest,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> ProjectResponse:
    return CreateProjectController.execute(current_user, project)
