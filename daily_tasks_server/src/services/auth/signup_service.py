from datetime import datetime

from psycopg2.extensions import connection

from daily_tasks_server.src.entity import User
from daily_tasks_server.src.models import UserSignupModel


class SignupService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, user_request: UserSignupModel) -> None:
        sql = ("INSERT INTO person(first_name, last_name, email, password, active_email, enable, created_at) VALUES("
               "%s, %s, %s, %s, %s, %s, %s)")

        user = User()
        user.change_first_name(user_request.first_name)
        user.change_last_name(user_request.last_name)
        user.change_email(user_request.email)
        user.encrypt_password(user_request.password)
        user.change_created_at(datetime.utcnow())
        user.enable_user()

        data = (
            user.first_name,
            user.last_name,
            user.email,
            user.password,
            user.active_email,
            user.enable,
            user.created_at,
        )

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)
