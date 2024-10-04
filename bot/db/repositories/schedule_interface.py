from abc import ABC, abstractmethod


class ISchedule(ABC):
    @abstractmethod
    async def get_schedule(self, day):
        raise NotImplementedError
