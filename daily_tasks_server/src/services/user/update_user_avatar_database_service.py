from psycopg2.extensions import connection


class UpdateUserAvatarDatabaseService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, email: str, avatar_url: str) -> None:
        sql = "UPDATE person SET avatar=%s WHERE email=%s"

        data = (
            avatar_url,
            email,
        )

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)
