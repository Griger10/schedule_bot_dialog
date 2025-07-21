from dishka import Provider, Scope, provide

from core.interfaces import TransactionManager, UserRepository
from core.interfaces.services.user_service import UserService
from services.user_service import UserServiceImpl


class UserServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def provide_user_service(
            self,
            user_repo: UserRepository,
            transaction_manager: TransactionManager,
    ) -> UserService:
        return UserServiceImpl(
            user_repo=user_repo,
            transaction_manager=transaction_manager,
        )
