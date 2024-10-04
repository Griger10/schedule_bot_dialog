from abc import ABC, abstractmethod


class IGroup(ABC):

    @abstractmethod
    async def get_groups(self):
        raise NotImplementedError

    @abstractmethod
    async def add_group(self, group_name):
        raise NotImplementedError

    @abstractmethod
    async def delete_group(self, group_name):
        raise NotImplementedError

    @abstractmethod
    async def set_group(self, group_id):
        raise NotImplementedError
