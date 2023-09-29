from fastapi import HTTPException, status
from psycopg2 import DataError, errorcodes

from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.projects.project_models import ProjectResponse
from daily_tasks_server.src.services.projects.get_project_by_id_service import GetProjectByIdService


class GetProjectByIdController:

    @staticmethod
    def execute(owner_id: str, project_id: str) -> ProjectResponse:
        try:
            database_session = DatabaseSession()

            with database_session.get_session() as session:
                get_project_by_id_service = GetProjectByIdService(session)
                return get_project_by_id_service.execute(owner_id, project_id)

        except DataError as e:
            error_code = status.HTTP_400_BAD_REQUEST
            error_message = f"Could not find project, reason: {e}"

            if errorcodes.INVALID_TEXT_REPRESENTATION:
                error_message = "Could not find project, reason: ID is invalid!"

            raise HTTPException(
                status_code=error_code,
                detail=error_message
            )

