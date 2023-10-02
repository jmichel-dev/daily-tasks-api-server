from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.task.task_model import TaskRequest, TaskResponse
from daily_tasks_server.src.services.task.update_task_service import UpdateTaskService


class UpdateTaskController:

    @staticmethod
    def execute(project_id: str, task_id: str, task_request: TaskRequest) -> TaskResponse:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            update_task_service = UpdateTaskService(session)
            task_updated = update_task_service.execute(project_id, task_id, task_request)

            session.commit()

            return task_updated
