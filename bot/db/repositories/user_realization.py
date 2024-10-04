from bot.db.repositories.user_interface import IUser
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.dialects.postgresql import insert as upsert


class UserRealization(IUser):
   def __init__(self, session: AsyncSession):
       self.session = session

    async def upsert_user(self, tg_id: int, username: str):
        stmt = upsert(User)