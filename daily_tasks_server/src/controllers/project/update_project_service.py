from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.projects.project_models import ProjectUpdateRequest, ProjectResponse
from daily_tasks_server.src.services.projects.update_project_service import UpdateProjectService


class UpdateProjectController:

    @staticmethod
    def execute(
            user: UserResponseModel,
            project_id: str,
            project_request: ProjectUpdateRequest
    ) -> ProjectResponse:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            update_project_service = UpdateProjectService(session)
            updated_project = update_project_service.execute(user.uid, project_id, project_request)

            session.commit()

            return updated_project
