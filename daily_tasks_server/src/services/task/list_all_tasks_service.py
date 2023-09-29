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
            task = TaskResponse()
            task.id = row[0]
            task.title = row[1]
            task.description = row[2]
            task.status = row[3]
            task.priority = row[4]
            task.start_date = row[5]
            task.end_date = row[6]
            task.created_at = row[7]
            task.updated_at = row[8]
            task.project_id = row[9]

            tasks.append(task)

        return TasksResponse(
            objects=tasks
        )
