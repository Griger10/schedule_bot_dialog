from core.interfaces import TransactionManager, UserRepository
from models import User


class UserServiceImpl:

    def __init__(
            self,
            user_repo: UserRepository,
            transaction_manager: TransactionManager
    ) -> None:
        self._user_repo = user_repo
        self._transaction_manager = transaction_manager

    async def add_user(
            self,
            tid: int,
            first_name: str,
            last_name: str | None,
            username: str | None
    ) -> None:
        await self._user_repo.upsert_user(
            tid=tid,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        await self._transaction_manager.commit()

    async def get_user(
            self,
            tid: int
    ) -> User | None:
        return await self._user_repo.get_user(tid=tid)
