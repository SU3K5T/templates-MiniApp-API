from fastapi import APIRouter
from app.core.s3_client import S3Client
from app.services.template_service import get_template_from_action

router = APIRouter(prefix='/templates')


@router.get('/{json_template_filename}')
async def get_template(json_template_filename: str):
  s3 = S3Client()
  data = await s3.get_json_file(json_template_filename)
  return data


