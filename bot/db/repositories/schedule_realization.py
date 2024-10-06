from bot.db import WeekType, Schedule, Lesson
from bot.db.repositories.group_realization import GroupRealization
from schedule_interface import ISchedule
from sqlalchemy import select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, join


class ScheduleRealization(ISchedule):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_schedule(self, telegram_id: int, day: int):
        type_of_week = self.get_week_type()
        group = await GroupRealization.get_group(self.session, telegram_id)
        s = aliased(Schedule)
        ls = aliased(Lesson)
        tables = join(ls, s, s.lesson_id == ls.id)
        query = (select(s.number_of_lesson, s.audience, ls.name).select_from(tables).
                 where(s.group == group, s.day == day, s.type == type_of_week)
                 .order_by(s.number_of_lesson)).distinct()
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_week_type(self):
        stmt = select(WeekType).select_from(WeekType)
        res = await self.session.execute(stmt)
        return res.scalar()
