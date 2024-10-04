from bot.db import User
from bot.db.repositories.user_interface import IUser
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert as upsert


class UserRealization(IUser):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def upsert_user(self, tg_id: int, username: str):
        stmt = upsert(User).values(telegram_id=tg_id, username=username)
        await self.session.execute(stmt)
        await self.session.commit()

    async def check_user(self, tg_id: int):
        stmt = select(User).where(tg_id=tg_id)
        user = await self.session.execute(stmt)
        return user.scalars().all()[0]
