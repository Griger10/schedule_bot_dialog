from bot.db import Group, User
from bot.db.repositories.group_interface import IGroup
from slugify import slugify
from sqlalchemy import delete, select, update
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession


class GroupRealization(IGroup):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_group(self, verbose_name):
        stmt = insert(Group).values(slug=slugify(verbose_name), name=verbose_name)
        await self.session.execute(stmt)
        await self.session.commit()

    async def delete_group(self, verbose_name):
        stmt = delete(Group).where(Group.slug == slugify(verbose_name))
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_groups(self):
        stmt = select(Group).select_from(Group)
        result = await self.session.execute(stmt)
        groups = result.scalars().all()
        return groups

    async def set_group(self, group_id: int, user_id: int):
        stmt = update(User).where(User.telegram_id == user_id).values(group=group_id)
        await self.session.execute(stmt)
        await self.session.commit()

    @staticmethod
    async def get_group(session, user_id):
        user = await session.get(User, user_id)
        return user.group
