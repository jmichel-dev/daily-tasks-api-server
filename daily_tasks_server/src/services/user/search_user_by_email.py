from psycopg2.extensions import connection
from fastapi import HTTPException, status

from daily_tasks_server.src.models import UserResponseModel
from daily_tasks_server.src.services.user.search_user_database_by_email_service import SearchUserDatabaseByEmailService


class SearchUserByEmail:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str) -> UserResponseModel:
        search_user_database_by_email_service = SearchUserDatabaseByEmailService(self.db_session)
        user = search_user_database_by_email_service.execute(email)

        return UserResponseModel(
            uid=user.uid,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            active_email=user.active_email,
            enable=user.enable,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
