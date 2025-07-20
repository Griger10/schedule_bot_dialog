from typing import Protocol

from models.user import User


class UserRepository(Protocol):

    async def upsert_user(self, tid: int, username: str) -> None: ...

    async def get_user(self, tid: int) -> User | None: ...
