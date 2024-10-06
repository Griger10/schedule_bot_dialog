from bot.db.base import Base
from sqlalchemy import Boolean, Enum, Column
from sqlalchemy.orm import Mapped, mapped_column


class WeekType(Base):
    __tablename__ = 'week_type'

    id: Mapped[int] = mapped_column(primary_key=True)
    type_code: Mapped[int] = mapped_column(default=0)

