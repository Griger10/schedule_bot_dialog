from bot.db.repositories.schedule_realization import ScheduleRealization
from bot.infrastructure.scheduler.taskiq_broker import broker
from sqlalchemy.ext.asyncio import AsyncSession


@broker.task
async def change_type_of_week(session: AsyncSession):
    schedule_repository = ScheduleRealization(session)
    await schedule_repository.change_week_type()


@broker.task(task_name='change_type_of_week_automation', schedule=[{'cron': '0 20 * * 5'}])
async def change_type_of_week_automation(session: AsyncSession):
    schedule_repository = ScheduleRealization(session)
    await schedule_repository.change_week_type()
