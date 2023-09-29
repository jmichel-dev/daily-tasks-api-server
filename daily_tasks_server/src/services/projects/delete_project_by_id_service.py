from psycopg2.extensions import connection


class DeleteProjectByIdService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, owner_id: str, project_id: str) -> None:
        sql = "DELETE FROM project WHERE owner_id=%s AND id=%s"
        data = (owner_id, project_id)

        cursor = self.db_session.cursor()
        cursor.execute()
        