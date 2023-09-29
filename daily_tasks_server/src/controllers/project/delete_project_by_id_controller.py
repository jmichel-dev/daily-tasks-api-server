from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services.projects.delete_project_by_id_service import DeleteProjectByIdService


class DeleteProjectByIdController:

    @staticmethod
    def execute(owner_id: str, project_id: str) -> None:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            delete_project_service = DeleteProjectByIdService(session)
            delete_project_service.execute(owner_id, project_id)
            session.commit()
