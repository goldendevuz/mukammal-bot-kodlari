from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.keyboards.reply import menu_start_keyboard

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n")
    await message.answer("Telefoningiz va Manzilingizni yuboring", reply_markup=menu_start_keyboard)
