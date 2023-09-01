from daily_tasks_server.src.config.database import DatabaseInterface
from daily_tasks_server.src.config.database.postgresql import PostgreSqlConnection


class DatabaseSession(DatabaseInterface):

    def __init__(self) -> None:
        connection = PostgreSqlConnection()
        self.session = connection.get_session()
