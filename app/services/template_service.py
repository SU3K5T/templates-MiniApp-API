from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.models.category import Category
from app.models.template import Template

async def get_template_from_action(db: AsyncSession, slug: str):
  template = await db.execute(select(Template).where(Template.template_slug == slug))
  return template.scalar_one_or_none()







  # query = select(Template).options(joinedload(Template.category)).where(Template.template_slug == slug)
  # template = await db.execute(query)
  # return {
  #   "category_info": template.category,
  #   "template_actions": template.scalar_one_or_none()
  #   }