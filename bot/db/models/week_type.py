from bot.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class WeekType(Base):
    __tablename__ = 'week_type'

    type_code: Mapped[bool] = mapped_column(default=False)

