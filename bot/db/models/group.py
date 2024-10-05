from bot.db.base import Base
from sqlalchemy.orm import mapped_column, Mapped


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    slug: Mapped[str]
    name: Mapped[str]
