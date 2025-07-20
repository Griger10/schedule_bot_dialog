from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class User(Base):
    __tablename__ = 'users'

    tid: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=False)
    first_name: Mapped[str] = mapped_column()
    phone_number: Mapped[str | None] = mapped_column(
        nullable=True,
        unique=True
    )
    last_name: Mapped[str | None] = mapped_column(nullable=True)
    username: Mapped[str | None] = mapped_column()
    group_name: Mapped[str | None] = mapped_column(nullable=True)
    group_slug: Mapped[str | None] = mapped_column(nullable=True)
