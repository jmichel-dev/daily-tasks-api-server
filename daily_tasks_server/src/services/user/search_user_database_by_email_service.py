from psycopg2.extensions import connection
from fastapi import HTTPException, status

from daily_tasks_server.src.entity import User
from daily_tasks_server.src.models import UserResponseModel


class SearchUserDatabaseByEmail:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str) -> User:
        sql = ("SELECT id,first_name,last_name,email,active_email,password_salt,password,enable,created_at,updated_at "
               "FROM person WHERE email=%s")
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
        password_salt = output[4]
        password = output[5]
        active_email = output[6]
        enable = output[7]
        created_at = output[8]
        updated_at = output[9]

        user = User()
        user.change_uid(uid)
        user.change_first_name(first_name)
        user.change_last_name(last_name)
        user.change_email(email)
        user.change_password_salt(password_salt)
        user.encrypted_password(password)
        user.change_active_email(active_email)
        user.change_enable(enable)
        user.change_created_at(created_at)
        user.change_updated_at(updated_at)

        return user
