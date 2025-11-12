from aiogram.filters import Filter
from aiogram import types


class IsPrivate(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == "private"