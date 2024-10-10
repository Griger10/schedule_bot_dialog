from typing import Callable, Awaitable, Dict, Any, cast

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message
from db.repositories.user_realization import UserRealization
from sqlalchemy.ext.asyncio import AsyncSession


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],
    ) -> Any:
        session: AsyncSession = data["session"]
        user_repository = UserRealization(session=session)
        event = cast(Message, event)
        user_id = event.from_user.id

        user = await user_repository.check_user(user_id)
        if user is None:
            username = event.from_user.username or 'Stranger'
            await user_repository.upsert_user(
                tg_id=event.from_user.id,
                username=event.from_user.username
            )
        return await handler(event, data)
