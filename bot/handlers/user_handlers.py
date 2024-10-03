from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import Dialog, Window

router = Router()


@router.message(Command(commands=['start']))
async def start(message: Message, ):
    pass
