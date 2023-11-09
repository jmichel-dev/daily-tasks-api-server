from fastapi.datastructures import UploadFile

from daily_tasks_server.src.config.database import DatabaseSession
from daily_tasks_server.src.services.user.upload_user_avatar_amazon_s3_service import UploadUserAvatarAmazonS3Service


class UpdateUserAvatarController:

    @staticmethod
    async def execute(email: str, avatar: UploadFile) -> str | None:
        avatar_url = await UploadUserAvatarAmazonS3Service.execute(avatar)
        print(avatar_url)

        return avatar_url
