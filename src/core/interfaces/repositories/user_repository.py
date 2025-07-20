from typing import Protocol

from models.user import User


class UserRepository(Protocol):

    async def upsert_user(
            self,
            tid: int,
            first_name: str,
            username: str | None,
            last_name: str | None
    ) -> None: ...

    async def get_user(self, tid: int) -> User | None: ...
