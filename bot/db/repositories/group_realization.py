from bot.db.repositories.group_interface import IGroup
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession


class GroupRealization(IGroup):
    def __init__(self, session: AsyncSession):
        self.session = session


    async def add_group(self):
        stmt = insert(Group).values()