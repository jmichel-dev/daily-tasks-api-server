from datetime import datetime


class ConfirmEmailService:

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def execute(self, user: str) -> None:
        sql = "UPDATE person SET active_email=true, updated_at=%s WHERE email = %s"

        with self.db_session as session:
            update_timestamp = datetime.utcnow()

            data = (update_timestamp, user,)

            cursor = session.cursor()
            cursor.execute(sql, data)
            session.commit()
