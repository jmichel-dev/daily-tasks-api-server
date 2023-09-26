from typing import Annotated

from psycopg2.extensions import connection
from fastapi import APIRouter, status, Depends

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.config.database import DatabaseInterface, DatabaseSession
from daily_tasks_server.src.controllers.project.lst_projects_by_owner_controller import ListProjectsByOwnerController
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.projects.project_models import ProjectResponse, ProjectRequest, ProjectsResponse
from daily_tasks_server.src.controllers.project.create_project_controller import CreateProjectController


router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=ProjectsResponse
)
def list_projects(current_user: Annotated[UserResponseModel, Depends(get_current_active_user)]) -> ProjectsResponse:
    return ListProjectsByOwnerController.execute(current_user)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=ProjectResponse,
    name="Create project"
)
def create_project(
        project: ProjectRequest,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> ProjectResponse:
    return CreateProjectController.execute(current_user, project)
