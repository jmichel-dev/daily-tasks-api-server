from io import BytesIO

from aiobotocore.session import get_session
from types_aiobotocore_s3 import S3Client


class S3Service(object):

    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, aws_region: str) -> None:
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_region = aws_region

    async def upload_file(self, fileobject: bytes, bucket: str, key: str) -> str | None:
        session = get_session()

        async with session.create_client(
            's3',
            region_name=self.aws_region,
            aws_secret_access_key=self.aws_secret_access_key,
            aws_access_key_id=self.aws_access_key_id
        ) as client:
            client: S3Client
            upload_object_response = await client.put_object(
                ACL="public-read",
                Bucket=bucket,
                Key=key,
                Body=fileobject
            )

            if upload_object_response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                return f"https://{bucket}.s3.{self.aws_region}.amazonaws.com/{key}"

            return None
