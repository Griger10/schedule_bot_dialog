from abc import ABC, abstractmethod


class ILesson(ABC):

    @abstractmethod
    async def get_lessons(self, lesson_name):
        raise NotImplementedError