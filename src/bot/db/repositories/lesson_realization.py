from db import Lesson
from db.repositories.lesson_interface import ILesson
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession


class LessonRealization(ILesson):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_lesson(self, lesson: str):
        stmt = insert(Lesson).values(name=lesson)
        await self.session.execute(stmt)
        await self.session.commit()
