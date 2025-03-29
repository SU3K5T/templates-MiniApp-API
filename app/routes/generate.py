import json
from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse
from app.services.doc_generator import DocxGenerator
from app.core.config import settings
from app.core.s3_client import S3Client

router = APIRouter(prefix='/generate')

@router.post('/')
async def generate_document(payload: dict = Body(...)):
    user_data = payload

    s3 = S3Client(bucket_name=settings.S3_FORMAT_TEMPLATES_BUCKET)
    template_data = await s3.get_json_file(user_data["S3FormatTemplateName"])

    # Генерируем документ
    generator = DocxGenerator(template_data, user_data)
    file_stream = generator.save_to_bytesio()
    return StreamingResponse(
        content=file_stream,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": "attachment; filename=contract.docx"}
    )
