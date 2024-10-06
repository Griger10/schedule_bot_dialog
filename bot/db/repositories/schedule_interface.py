from abc import ABC, abstractmethod


class ISchedule(ABC):
    @abstractmethod
    async def get_schedule(self, telegram_id, day):
        raise NotImplementedError

    @abstractmethod
    async def get_week_type(self):
        raise NotImplementedError
