from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from app.models.category import Category


async def get_all_categories(db: AsyncSession):
    result = await db.execute(select(Category))
    return result.scalars().all()

async def get_actions_from_category(db: AsyncSession, slug: str):
    query = select(Category).options(joinedload(Category.templates)).where(Category.slug == slug)
    category = await db.execute(query)
    return category.unique().scalar_one_or_none()