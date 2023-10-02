from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.task.task_model import TaskResponse
from daily_tasks_server.src.services.task.list_task_by_id_service import ListTaskByIdService


class ListTaskByIdController:

    @staticmethod
    def execute(project_id: str, task_id: str) -> TaskResponse:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            list_task_by_id_service = ListTaskByIdService(session)

            return list_task_by_id_service.execute(project_id, task_id)
