from psycopg2.extensions import connection

from daily_tasks_server.src.models.task.task_model import TaskRequest, TaskResponse


class CreateTaskService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, project_id: str, task_request: TaskRequest) -> TaskResponse:
        sql = ("INSERT INTO task(title,description,status,priority,start_date,end_date,project_id) VALUES(%s,%s,%s,%s,"
               "%s,%s,%s) RETURNING id,title,description,status,priority,start_date,end_date,created_at,updated_at")

        data = (
            task_request.title,
            task_request.description,
            task_request.status,
            task_request.priority,
            task_request.start_date,
            task_request.end_date,
            project_id
        )

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        row = cursor.fetchone()

        print(row)

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

