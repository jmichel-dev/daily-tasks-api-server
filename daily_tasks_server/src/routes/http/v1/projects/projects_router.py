from typing import Annotated

from fastapi import APIRouter, status, Depends, HTTPException

from daily_tasks_server.src.config.authentication import get_current_active_user
from daily_tasks_server.src.controllers.project.get_project_by_id_controller import GetProjectByIdController
from daily_tasks_server.src.controllers.project.lst_projects_by_owner_controller import ListProjectsByOwnerController
from daily_tasks_server.src.controllers.project.update_project_service import UpdateProjectController
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.projects.project_models import ProjectResponse, ProjectRequest, ProjectsResponse, \
    ProjectUpdateRequest
from daily_tasks_server.src.controllers.project.create_project_controller import CreateProjectController


router = APIRouter()


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=ProjectsResponse,
    name="List projects by user"
)
def list_projects(current_user: Annotated[UserResponseModel, Depends(get_current_active_user)]) -> ProjectsResponse:
    return ListProjectsByOwnerController.execute(current_user)


@router.get(
    "/{project_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProjectResponse,
    name="Get project by id and user"
)
def list_projects(
        project_id: str,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)]
) -> ProjectResponse:
    return GetProjectByIdController.execute(current_user.uid, project_id)


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


@router.put(
    "/{project_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProjectResponse,
    name="Update project"
)
def update_project(
        project_id: str,
        project_request: ProjectUpdateRequest,
        current_user: Annotated[UserResponseModel, Depends(get_current_active_user)],
) -> ProjectResponse:
    return UpdateProjectController.execute(current_user, project_id, project_request)
