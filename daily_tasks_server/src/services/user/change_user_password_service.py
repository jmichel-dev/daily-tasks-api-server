import bcrypt
from psycopg2.extensions import connection

from daily_tasks_server.src.services.auth.change_password_by_email_service import ChangePasswordByEmailService


class ChangeUserPasswordService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str, password_salt: bytes, password: str) -> None:
        change_password_by_email_service = ChangePasswordByEmailService(self.db_session)
        change_password_by_email_service.execute(email, password, password_salt)
