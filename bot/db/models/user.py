from db.base import Base
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'users'

    telegram_id = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None]
    group: Mapped[int | None]
