from psycopg2.extensions import connection

from daily_tasks_server.src.models.task.task_model import TaskRequestByProject, TasksResponse, TaskResponse


class ListAllTasksService:

    def __init__(self, db_session: connection):
        self.db_session = db_session

    def execute(self, project_id: str) -> TasksResponse:
        sql = "SELECT * FROM task WHERE project_id=%s"
        data = (project_id,)
        tasks = []

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        result = cursor.fetchall()
        cursor.close()

        for row in result:
            task = TaskResponse(
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

            tasks.append(task)

        return TasksResponse(
            objects=tasks
        )
