from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.models.auth.user_response_model import UserResponseModel
from daily_tasks_server.src.models.task.task_model import TaskRequest, TaskResponse
from daily_tasks_server.src.services.user.create_task_service import CreateTaskService


class CreateTaskController:

    @staticmethod
    def execute(project_id: str, user: UserResponseModel, task_request: TaskRequest) -> TaskResponse:
        database_session = DatabaseSession()

        with database_session.get_session() as session:
            create_task_service = CreateTaskService(session)

            task = create_task_service.execute(project_id, task_request)
            session.commit()

            return task
