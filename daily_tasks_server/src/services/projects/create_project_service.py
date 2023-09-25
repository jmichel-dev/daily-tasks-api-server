from psycopg2.extensions import connection

from daily_tasks_server.src.models.projects.project_models import ProjectResponse, ProjectRequest


class CreateProjectService:

    def __init__(self, db_session: connection) -> None:
        self.db_session = db_session

    def execute(self, owner_id: str, project: ProjectRequest) -> ProjectResponse:

        sql = ("INSERT INTO project(title, description, owner_id) VALUES(%s, %s, %s) RETURNING id, created_at, "
               "updated_at")

        data = (project.title, project.description, owner_id)

        cursor = self.db_session.cursor()
        cursor.execute(sql, data)

        output = cursor.fetchone()
        cursor.close()

        project_id = output[0]
        created_at = output[1]
        updated_at = output[2]

        return ProjectResponse(
            id=project_id,
            title=project.title,
            description=project.description,
            owner=owner_id,
            created_at=created_at,
            updated_at=updated_at
        )
