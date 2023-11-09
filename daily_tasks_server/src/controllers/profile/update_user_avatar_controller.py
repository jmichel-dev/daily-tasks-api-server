from fastapi.datastructures import UploadFile

from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services.user.update_user_avatar_database_service import UpdateUserAvatarDatabaseService
from daily_tasks_server.src.services.user.upload_user_avatar_amazon_s3_service import UploadUserAvatarAmazonS3Service


class UpdateUserAvatarController:

    @staticmethod
    async def execute(email: str, avatar: UploadFile) -> str | None:
        db_session = DatabaseSession()

        with db_session.get_session() as session:
            avatar_url = await UploadUserAvatarAmazonS3Service.execute(avatar)
            update_user_avatar_database_service = UpdateUserAvatarDatabaseService(session)

            update_user_avatar_database_service.execute(email, avatar_url)

            session.commit()

            return avatar_url
