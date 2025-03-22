from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from app.core.database import init_tables, ins

from app.routes import categories as categories_router
# from app.routes import json_files as json_router
from app.routes import templates as templates_router
from app.routes import generate as generate_router

from app.core.s3_client import S3Client

app = FastAPI()

# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Можно указать конкретные домены
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def setup_database():
   await init_tables()
   await ins()
#    s3 = S3Client()
#    await s3.upload_file('app/data/lease_agreement.json')



app.include_router(categories_router.router, tags=["Categories"])
# app.include_router(json_router.router, tags=["JSON Files"])
app.include_router(templates_router.router, tags=["Templates"])
app.include_router(generate_router.router, tags=["Generate document"])

