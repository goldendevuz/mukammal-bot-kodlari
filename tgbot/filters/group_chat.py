from aiogram.filters import Filter
from aiogram import types

class IsGroup(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in ("group", "supergroup")
