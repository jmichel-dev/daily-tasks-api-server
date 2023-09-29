from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.task.task_model import TaskRequestByProject, TasksResponse
from daily_tasks_server.src.services.task.list_all_tasks_service import ListAllTasksService


class ListAllTasksController:

    @staticmethod
    def execute(user: UserResponseModel, project_id: str) -> TasksResponse:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            list_tasks_service = ListAllTasksService(session)

            return list_tasks_service.execute(project_id)
