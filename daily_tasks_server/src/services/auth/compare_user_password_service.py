from psycopg2.extensions import connection
from fastapi import HTTPException, status

from daily_tasks_server.src.utils.hash_password import check


class CompareUserPasswordService:

    def __init__(self, db_session: connection):
        self.db_session = db_session

    def execute(self, email: str, password: str) -> bool:
        sql = "SELECT password FROM person WHERE email=%s"
        data = (email,)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        result = cursor.fetchone()
        cursor.close()

        if result is None or len(result) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email/password invalid"
            )

        hashed_password = result[0]

        return check(password, hashed_password)
