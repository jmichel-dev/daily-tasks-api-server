from psycopg2.extensions import connection


class DeleteTaskService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, project_id: str, task_id: str) -> None:
        sql = "DELETE FROM task WHERE project_id=%s and id=%s"
        data = (project_id, task_id,)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)
