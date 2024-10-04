from schedule_interface import ISchedule
from sqlalchemy.ext.asyncio import AsyncSession


class ScheduleRealization(ISchedule):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_schedule(self, day: int):
        return None
