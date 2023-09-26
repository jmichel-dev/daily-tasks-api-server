from datetime import datetime

from psycopg2.extensions import connection

from daily_tasks_server.src.models.projects.project_models import ProjectResponse, ProjectUpdateRequest


class UpdateProjectService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, owner_id: str, project_id: str, project_request: ProjectUpdateRequest) -> ProjectResponse:

        sql = ("UPDATE project SET title=%s,description=%s,updated_at=%s WHERE owner_id=%s AND id=%s RETURNING "
               "created_at")
        updated_at = datetime.utcnow()

        data = (
            project_request.title,
            project_request.description,
            updated_at,
            owner_id,
            project_id
        )

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        output = cursor.fetchone()
        cursor.close()

        return ProjectResponse(
            id=project_id,
            title=project_request.title,
            description=project_request.description,
            owner=owner_id,
            created_at=output[0],
            updated_at=updated_at
        )
