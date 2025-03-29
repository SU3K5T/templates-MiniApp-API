from fastapi import APIRouter
from app.core.s3_client import S3Client
from app.core.config import settings

router = APIRouter(prefix='/templates')


@router.get('/{json_template_filename}')
async def get_template(json_template_filename: str):
  s3 = S3Client(bucket_name=settings.S3_EMPTY_TEMPLATES_BUCKET)
  data = await s3.get_json_file(json_template_filename)
  return data


