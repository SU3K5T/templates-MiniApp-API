from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

class Template(Base):
    __tablename__ = "templates"

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    template_slug: Mapped[str] = mapped_column()
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    json_template_filename: Mapped[str] = mapped_column() # Ссылка для json, который будет приходить для заполнения
    format_json_filename: Mapped[str] = mapped_column()  # Ссылка на шаблон документа в json
    category: Mapped["Category"] = relationship("Category", back_populates="templates")