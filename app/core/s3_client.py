from contextlib import asynccontextmanager
import json
from typing import Any, Dict
from aiobotocore.session import get_session
from aiobotocore.config import AioConfig
from app.core.config import settings

class S3Client:

    def __init__(
            self,
            access_key: str = settings.S3_ACCESS_KEY,
            secret_key: str = settings.S3_SECRET_KEY,
            endpoint_url: str = settings.S3_ENDPOINT,
            bucket_name: str = settings.S3_BUCKET,
            cert_path: str = settings.S3_CERT_PATH
    ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url,
            "verify": cert_path,
            "config": AioConfig(
            s3={
                "addressing_style": "virtual",  # Важно для vHosted
                "signature_version": "s3v4"
            }
            )
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

    async def upload_file(
            self,
            file_path: str,
    ):
        object_name = file_path.split("/")[-1]
        async with self.get_client() as client:
            with open(file_path, "rb") as file:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file,
                )

    async def get_json_file(
        self, 
        object_name: str,
        encoding: str = "utf-8"
    ) -> Dict[str, Any]:
        """
        Скачивает и возвращает JSON файл из S3
        """
        async with self.get_client() as client:

            response = await client.get_object(
                Bucket=self.bucket_name,
                Key=object_name+".json"
            )
            data = await response["Body"].read()
            return json.loads(data.decode(encoding))
