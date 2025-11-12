import io

from aiogram import Bot, Router, types
from aiogram.types import Message
from aiogram.filters.command import Command

from tgbot.filters import IsGroup, IsAdmin

edit_group_router = Router()


@edit_group_router.message(
    IsGroup(),
    Command("set_photo", prefix=("!", "/")),
    IsAdmin(),
)
async def set_new_photo(message: Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    await message.chat.set_photo(photo=input_file)

@edit_group_router.message(
    IsGroup(),
    Command("set_title", prefix=("!", "/")),
    IsAdmin(),
)
async def set_new_title(message: Message, bot: Bot):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    await bot.set_chat_title(message.chat.id, title=title)


@edit_group_router.message(
    IsGroup(),
    Command("set_description", prefix=("!", "/")),
    IsAdmin(),
)
async def set_new_description(message: Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)
