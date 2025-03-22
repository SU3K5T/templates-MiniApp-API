import json
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from app.core.config import settings

from app.models.base import Base
from app.models.category import Category
from app.models.template import Template


DATABASE_URL = settings.GET_DATABASE_URL

print(DATABASE_URL)

# Создаем движок SQLAlchemy
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаем базу данных
async def init_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    

# Создаем сессию для работы с БД
AsyncSessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

async def ins():
    with open('app/core/categories.json', 'r', encoding='utf-8') as file:
        category_data = json.load(file)

    with open('app/core/actions.json', 'r', encoding='utf-8') as file:
        actions_data = json.load(file)

 
    async with AsyncSessionLocal() as session:
        
        for item in category_data:
            session.add(Category(
                slug=item['slug'],
                title=item['title'],
                description=item['description']
            ))


        for item in actions_data:
            session.add(Template(
                category_id=item['category_id'],
                template_slug=item['template_slug'],
                title=item['title'],
                description=item['description'],
                json_template_filename=item['json_template_filename'],
                format_json_filename=item['format_json_filename']
            ))
            
        await session.flush()
        await session.commit()


# Функция для получения сессии
async def get_async_session():
    async with AsyncSessionLocal() as session:
        yield session

