from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

class Category(Base):
  __tablename__ = "categories"

  id: Mapped[int] = mapped_column(primary_key=True)
  slug: Mapped[str] = mapped_column()
  title: Mapped[str] = mapped_column()
  description: Mapped[str] = mapped_column()
  templates: Mapped[list["Template"]] = relationship("Template", back_populates="category")

  