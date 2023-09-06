from psycopg2 import connect
from psycopg2.extensions import connection

from daily_tasks_server.src.config import Config


class PostgreSqlConnection:

    def __init__(self) -> None:
        user = Config.DATABASE_USER
        password = Config.DATABASE_PASSWORD
        host = Config.DATABASE_HOST
        port = Config.DATABASE_PORT
        database = Config.DATABASE_NAME

        self.__session = connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def get_session(self) -> connection:
        return self.__session
