from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.projects.project_models import ProjectResponse, ProjectRequest
from daily_tasks_server.src.services.projects.create_project_service import CreateProjectService


class CreateProjectController:

    @staticmethod
    def execute(owner: UserResponseModel, project: ProjectRequest) -> ProjectResponse:
        db_session = DatabaseSession()

        with db_session.get_session() as session:
            create_project_service = CreateProjectService(session)
            project_response = create_project_service.execute(owner.uid, project)

            session.commit()
            return project_response
