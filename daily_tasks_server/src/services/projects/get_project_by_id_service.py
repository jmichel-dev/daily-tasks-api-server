from psycopg2.extensions import connection

from daily_tasks_server.src.models.projects.project_models import ProjectResponse


class GetProjectByIdService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, owner_id: str, project_id: str) -> ProjectResponse | None:
        sql = "SELECT title,description,created_at,updated_at FROM project WHERE owner_id=%s AND id=%s"
        data = (owner_id, project_id)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)
        result = cursor.fetchone()
        cursor.close()

        if result is None or len(result) < 0:
            return None

        title = result[0]
        description = result[1]
        created_at = result[2]
        updated_at = result[3]

        return ProjectResponse(
            id=project_id,
            title=title,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            owner=owner_id
        )
