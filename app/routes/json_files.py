from fastapi import APIRouter, UploadFile, HTTPException, Depends
from app.core.s3_client import upload_json, get_json_url
import json

router = APIRouter(prefix="/upload")

@router.post("/")
async def upload_json_file(file: UploadFile):
    """Эндпоинт для загрузки JSON-файла в Selectel S3"""
    if file.content_type != "application/json":
        raise HTTPException(status_code=400, detail="Можно загружать только JSON-файлы")

    file_data = await file.read()
    try:
        json.loads(file_data)  # Проверяем, что это корректный JSON
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Некорректный JSON")

    file_url = upload_json(file.filename, file_data)
    return {"file_url": file_url}

# @router.get("/files/{file_name}")
# async def get_json_file_url(file_name: str):
#     """Эндпоинт для получения ссылки на JSON-файл"""
#     return {"file_url": get_json_url(file_name)}