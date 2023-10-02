from psycopg2.extensions import connection

from fastapi import HTTPException, status

from daily_tasks_server.src.models.task.task_model import TaskResponse


class ListTaskByIdService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, project_id: str, task_id: str) -> TaskResponse:
        sql = "SELECT * FROM task WHERE project_id=%s AND id=%s"
        data = (project_id, task_id)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        row = cursor.fetchone()

        if row is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Could not find task {task_id} in project {project_id}"
            )

        return TaskResponse(
            id=row[0],
            title=row[1],
            description=row[2],
            status=row[3],
            priority=row[4],
            start_date=row[5],
            end_date=row[6],
            created_at=row[7],
            updated_at=row[8],
            project_id=project_id,
        )
    