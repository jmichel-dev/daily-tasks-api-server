from psycopg2.extensions import connection


class DisableTokenService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, token: str) -> None:

        sql = "UPDATE tokens SET valid=false WHERE token = %s"
        data = (token,)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

