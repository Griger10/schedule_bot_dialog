from aiogram import BaseMiddleware
from sqlalchemy.ext.asyncio import AsyncSession


class TypeOfWeekMiddleware(BaseMiddleware):

    def __init__(self):
        super().__init__()

    async def __call__(self, handler, event, data):
        session: AsyncSession = data['session']
