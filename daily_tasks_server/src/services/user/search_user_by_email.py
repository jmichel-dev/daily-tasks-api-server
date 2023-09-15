from psycopg2.extensions import connection
from fastapi import HTTPException, status

from daily_tasks_server.src.models import UserResponseModel


class SearchUserByEmail:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str) -> UserResponseModel:
        sql = ("SELECT id,first_name,last_name,email,active_email,enable,created_at,updated_at FROM person WHERE "
               "email=%s")
        data = (email,)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        output = cursor.fetchone()
        cursor.close()

        if output is None or len(output) == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Could not find user by email {email}"
            )

        uid = output[0]
        first_name = output[1]
        last_name = output[2]
        email = output[3]
        active_email = output[4]
        enable = output[5]
        created_at = output[6]
        updated_at = output[7]

        return UserResponseModel(
            uid=uid,
            first_name=first_name,
            last_name=last_name,
            email=email,
            active_email=active_email,
            enable=enable,
            created_at=created_at,
            updated_at=updated_at,
        )
