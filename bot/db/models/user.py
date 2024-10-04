from bot.db.base import Base
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    telegram_id = mapped_column(BigInteger, index=True)
    username: Mapped[str]
    group: Mapped[int | None]
