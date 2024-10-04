from datetime import datetime

from bot.db import Base
from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column


class Lesson(Base):
    __tablename__ = 'lessons'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
