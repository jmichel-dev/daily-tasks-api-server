from datetime import datetime

from psycopg2.extensions import connection

from daily_tasks_server.src.utils import hash_password


class ChangePasswordByEmailService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str, password: str, password_salt: bytes) -> None:

        encrypted_password = hash_password.hashing(password, password_salt)
        updated_at = datetime.utcnow()

        sql = "UPDATE person SET password_salt=%s,password=%s,updated_at=%s WHERE email=%s"
        data = (
            password_salt.decode("utf-8"),
            encrypted_password,
            updated_at,
            email
        )

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)


