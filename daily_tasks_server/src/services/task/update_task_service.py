from datetime import datetime

from psycopg2.extensions import connection

from daily_tasks_server.src.models.task.task_model import TaskRequest, TaskResponse


class UpdateTaskService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, project_id: str, task_id: str, task_request: TaskRequest) -> TaskResponse:
        sql = ("UPDATE task SET title=%s,description=%s,status=%s,priority=%s,start_date=%s,end_date=%s,updated_at=%s "
               "WHERE project_id=%s AND id=%s RETURNING title,description,status,priority,start_date,end_date,"
               "created_at,updated_at")
        data = (
            task_request.title,
            task_request.description,
            task_request.status,
            task_request.priority,
            task_request.start_date,
            task_request.end_date,
            datetime.utcnow(),
            project_id,
            task_id,
        )

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        result = cursor.fetchone()
        cursor.close()

        return TaskResponse(
            id=task_id,
            title=result[0],
            description=result[1],
            status=result[2],
            priority=result[3],
            start_date=result[4],
            end_date=result[5],
            created_at=result[6],
            updated_at=result[7],
        )


