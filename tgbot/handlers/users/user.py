import logging

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    await message.answer(f"Assalom alaykum, {message.from_user.full_name}, do'konimizga xush kelibsiz!",reply_markup=menuStart)
