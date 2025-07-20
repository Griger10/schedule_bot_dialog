from typing import Protocol

from models import User


class UserService(Protocol):
    async def add_user(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None: ...

    async def get_user(
            self,
            tid: int
    ) -> User | None: ...
