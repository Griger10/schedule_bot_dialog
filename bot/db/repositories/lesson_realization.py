from bot.db import Lesson, Schedule
from bot.db.repositories.lesson_interface import ILesson
from sqlalchemy import insert, select, or_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import aliased, join


class LessonRealization(ILesson):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_lesson(self, lesson: str):
        stmt = insert(Lesson).values(name=lesson)
        await self.session.execute(stmt)
        await self.session.commit()

    async def get_lessons(self, telegram_id, type_of_week, day):
        types_of_week = {'numerator': 1, 'denominator': 2}
        group = await get_group(self.session, telegram_id)
        s = aliased(Schedule)
        ls = aliased(Lesson)
        tables = join(ls, s, s.lesson_id == ls.id)
        query = (select(s.number_of_lesson, s.audience, ls.name).select_from(tables).
                 where(s.group == group, s.day == days[day[1:]],
                       or_(s.type.is_(None), s.type == types_of_week[type_of_week]))
                 .order_by(s.number_of_lesson)).distinct()
        result = await self.session.execute(query)
        return result.all()
