import os
import uuid

from fastapi.datastructures import UploadFile

from daily_tasks_server.src.config import Config
from daily_tasks_server.src.config.s3_service import S3Service


class UploadUserAvatarAmazonS3Service:

    @staticmethod
    async def execute(file_object: UploadFile) -> str:
        filename = file_object.filename
        split_file_name = os.path.splitext(filename)
        filename_without_extension = split_file_name[0]
        file_unique_name = f"{str(uuid.uuid4())}-{filename_without_extension}"
        file_extension = split_file_name[1]
        data = await file_object.read()
        aws_filename = f"{file_unique_name}{file_extension}"

        s3_service = S3Service(
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
            aws_region=Config.AWS_REGION,
        )
        uploaded_file_url = await s3_service.upload_file(fileobject=data, bucket="dailytasks009", key=aws_filename)

        return uploaded_file_url

