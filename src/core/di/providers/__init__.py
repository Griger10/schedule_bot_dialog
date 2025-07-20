from core.di.providers.bot import BotProvider
from core.di.providers.config import ConfigProvider
from core.di.providers.database import DatabaseProvider
from core.di.providers.transaction_manager import TransactionManagerProvider
from core.di.providers.user_repository import UserRepositoryProvider
from core.di.providers.user_service import UserServiceProvider


def get_providers():
    return [
        BotProvider(),
        ConfigProvider(),
        DatabaseProvider(),
        TransactionManagerProvider(),
        UserRepositoryProvider(),
        UserServiceProvider(),
    ]
