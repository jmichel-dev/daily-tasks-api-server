from datetime import datetime

from psycopg2.extensions import connection


class ConfirmEmailService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, user: str) -> None:
        sql = "UPDATE person SET active_email=true, updated_at=%s WHERE email = %s"

        update_timestamp = datetime.utcnow()

        data = (update_timestamp, user,)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)
