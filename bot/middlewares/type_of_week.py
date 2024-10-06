from aiogram import BaseMiddleware
from bot.db.repositories.schedule_realization import ScheduleRealization
from sqlalchemy.ext.asyncio import AsyncSession


class TypeOfWeekMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()

    async def __call__(self, handler, event, data):
        session: AsyncSession = data['session']
        schedule_repository = ScheduleRealization(session)
        type_of_week = await schedule_repository.get_week_type()
        data['type_of_week'] = type_of_week
        return await handler(event, data)

