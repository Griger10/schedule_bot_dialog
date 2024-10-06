from bot.db.repositories.schedule_realization import ScheduleRealization
from bot.infrastructure.scheduler.taskiq_broker import broker
from sqlalchemy.ext.asyncio import AsyncSession


@broker.task
async def change_type_of_week(session: AsyncSession):
    schedule_repository = ScheduleRealization(session)
    await schedule_repository.change_week_type()

