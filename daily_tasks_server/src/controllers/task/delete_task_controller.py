from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services.task.delete_task_service import DeleteTaskService


class DeleteTaskController:

    @staticmethod
    def execute(project_id: str, task_id: str):
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            delete_task_service = DeleteTaskService(session)
            delete_task_service.execute(project_id, task_id)

            session.commit()
