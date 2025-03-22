from datetime import datetime
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from app.models.base import Base

class Generated_document(Base):
  __tablename__ = "generated_documents"

  id: Mapped[int] = mapped_column(primary_key=True)
  template_id: Mapped[int] = mapped_column(ForeignKey("templates.id"))
  created_at: Mapped[DateTime] = mapped_column(default=datetime.now)
  docx_url = Mapped[str] = mapped_column()

