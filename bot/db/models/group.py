from bot.db import Base
from sqlalchemy.orm import mapped_column, Mapped


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True)
    slug: Mapped[str]
    verbose_name: Mapped[str]
