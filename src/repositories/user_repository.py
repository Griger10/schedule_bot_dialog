from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert as upsert

from models import User


class UserRepositoryImpl:
    model: type[User] = User

    def __init__(self, session: AsyncSession):
        self._session = session

    async def upsert_user(
            self,
            tid: int,
            first_name: str,
            username: str | None,
            last_name: str | None,
    ):
        stmt = upsert(self.model).values(
            tid=tid,
            first_name=first_name,
            last_name=last_name,
            username=username,
        )
        await self._session.execute(stmt)
        await self._session.commit()

    async def get_user(self, tid: int) -> User | None:
        stmt = select(self.model).where(
            self.model.tid == tid
        )

        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()
