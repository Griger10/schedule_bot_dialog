from abc import ABC, abstractmethod


class ILesson(ABC):

    @abstractmethod
    async def add_lesson(self, lesson):
        raise NotImplementedError