from db.repositories.schedule_realization import ScheduleRealization
from infrastructure.scheduler.taskiq_broker import broker
from utils.db_connection import load_connection
from sqlalchemy.ext.asyncio import AsyncSession


@broker.task
async def change_type_of_week():
    session = await load_connection()
    schedule_repository = ScheduleRealization(session)

    await schedule_repository.change_week_type()


@broker.task(task_name='change_type_of_week_automation', schedule=[{'cron': '0 20 * * 5'}])
async def change_type_of_week_automation():
    session = await load_connection()
    schedule_repository = ScheduleRealization(session)
    await schedule_repository.change_week_type()
