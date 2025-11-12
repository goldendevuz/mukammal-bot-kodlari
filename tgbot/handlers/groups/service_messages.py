from aiogram import F, Bot, Router, types
from aiogram.types import Message

from tgbot.filters import IsGroup

service_messages_router = Router()


@service_messages_router.message(IsGroup(), F.new_chat_members)
async def new_member(message: Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Xush kelibsiz, {members}.")


@service_messages_router.message(IsGroup(), F.left_chat_member)
async def banned_member(message: Message, bot: Bot):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi "
                             f"Admin: {message.from_user.get_mention(as_html=True)}.")