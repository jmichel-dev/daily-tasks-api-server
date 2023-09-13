from datetime import datetime

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.services import JWTService


class GenerateAndSaveTokenService:

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def execute(self, email: str) -> str:
        payload = {
            "email": email
        }

        token = JWTService.generate(payload=payload, expiration=Config.JWT_ACTIVATE_EMAIL_TOKEN_EXPIRATION)
        created_at = datetime.utcnow()

        sql = "INSERT INTO tokens(token, created_at) VALUES(%s, %s)"

        data = (token, created_at)

        with self.db_session as session:
            cursor = session.cursor()
            cursor.execute(sql, data)
            session.commit()

        return token

