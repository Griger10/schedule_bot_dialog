from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class ISchedule(ABC):
    @abstractmethod
    async def get_schedule(self, day):
        return NotImplemented
