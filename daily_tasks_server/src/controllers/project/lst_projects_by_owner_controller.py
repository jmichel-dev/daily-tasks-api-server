from psycopg2.extensions import connection

from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.projects.project_models import ProjectsResponse
from daily_tasks_server.src.services.projects.list_projects_by_owner_service import ListProjectsByOwnerService


class ListProjectsByOwnerController:

    @staticmethod
    def execute(owner: UserResponseModel) -> ProjectsResponse:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            list_projects_by_owner_service = ListProjectsByOwnerService(session)

            return list_projects_by_owner_service.execute(owner.uid)
