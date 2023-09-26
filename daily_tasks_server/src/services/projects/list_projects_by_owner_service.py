from psycopg2.extensions import connection
from daily_tasks_server.src.models.projects.project_models import ProjectsResponse, ProjectResponse


class ListProjectsByOwnerService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, owner_id: str) -> ProjectsResponse | None:

        sql = "SELECT id,title,description,created_at,updated_at FROM project WHERE owner_id=%s"
        data = (owner_id,)
        result = []

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        rows = cursor.fetchall()

        if not rows:
            return None

        for row in rows:
            uid = row[0]
            title = row[1]
            description = row[2]
            created_at = row[3]
            updated_at = row[4]

            project_response = ProjectResponse(
                id=uid,
                title=title,
                description=description,
                owner=owner_id,
                created_at=created_at,
                updated_at=updated_at
            )

            result.append(project_response)

        return ProjectsResponse(objects=result)

