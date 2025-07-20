from abc import ABC, abstractmethod


class IUser(ABC):

    @abstractmethod
    async def upsert_user(self, tg_id: int, username: str):
        raise NotImplementedError

    @abstractmethod
    async def check_user(self, tg_id: int):
        raise NotImplementedError
