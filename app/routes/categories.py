from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_async_session
from app.services.category_service import get_all_categories, get_actions_from_category

router = APIRouter(prefix='/categories')

@router.get('/')
async def get_all_categories_handler(db: AsyncSession = Depends(get_async_session)):
  categories = await get_all_categories(db)
  return categories

@router.get('/{slug}')
async def get_category_actions(slug: str, db: AsyncSession = Depends(get_async_session)):
  templates = await get_actions_from_category(db, slug)
  return templates