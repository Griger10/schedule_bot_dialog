from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from core.interfaces import TransactionManager
from repositories import TransactionManagerImpl


class TransactionManagerProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.REQUEST)
    async def get_repository(self, session: AsyncSession) -> TransactionManager:
        return TransactionManagerImpl(session)
