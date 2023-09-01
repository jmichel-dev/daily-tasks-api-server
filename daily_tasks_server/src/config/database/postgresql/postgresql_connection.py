from psycopg2 import connect
from psycopg2.extensions import connection


class PostgreSqlConnection:

    def __init__(self) -> None:
        user = "todo"
        password = "todo"
        host = "localhost"
        port = 5432
        database = "todo"

        self.__session = connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )

    def get_session(self) -> connection:
        return self.__session
