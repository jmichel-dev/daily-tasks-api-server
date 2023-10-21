from typing import Dict
from datetime import datetime

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.services import JWTService


class GenerateAndSaveTokenService:

    def __init__(self, db_session) -> None:
        self.db_session = db_session

    def execute(self, payload: Dict, expiration_time: datetime) -> str:

        token = JWTService.generate(payload=payload, expiration=expiration_time)
        created_at = datetime.utcnow()

        sql = "INSERT INTO tokens(token, created_at) VALUES(%s, %s)"

        data = (token, created_at)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        return token

