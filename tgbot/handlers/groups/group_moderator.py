import asyncio
import datetime
import re

from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters.command import Command

from tgbot.filters import IsGroup, IsAdmin

group_moderator_router = Router()

# =======================
# /ro !ro (read-only)
# =======================
@group_moderator_router.message(
    IsGroup(),
    Command("ro", prefix=("!", "/")),
    IsAdmin(),
)
async def read_only_mode(message: Message):
    # Check if replied
    if not message.reply_to_message:
        return await message.reply("❌ Iltimos, foydalanuvchining xabariga reply qiling!")

    member = message.reply_to_message.from_user
    member_id = member.id

    # Parse time and comment
    command_parse = re.compile(r"(!ro|/ro)(?:\s+(\d+))?(?:\s+(.*))?")
    parsed = command_parse.match(message.text or "")
    time = int(parsed.group(2)) if parsed and parsed.group(2) else 5
    comment = parsed.group(3) if parsed and parsed.group(3) else "-"

    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    # Read-only permissions
    permissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_change_info=False,
        can_invite_users=False,
        can_pin_messages=False,
    )

    try:
        await message.chat.restrict(
            user_id=member_id,
            permissions=permissions,
            until_date=until_date
        )
        await message.reply_to_message.delete()
    except Exception as err:
        return await message.answer(f"Xatolik! {err}")

    await message.answer(
        f"✅ Foydalanuvchi {member.full_name} {time} minut yozish huquqidan mahrum qilindi.\n"
        f"Sabab: <b>{comment}</b>"
    )

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


# =======================
# /unro !unro (undo read-only)
# =======================
@group_moderator_router.message(
    IsGroup(),
    Command("unro", prefix=("!", "/")),
    IsAdmin(),
)
async def undo_read_only_mode(message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Iltimos, foydalanuvchining xabariga reply qiling!")

    member = message.reply_to_message.from_user
    member_id = member.id

    permissions = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )

    await message.chat.restrict(
        user_id=member_id,
        permissions=permissions,
        until_date=0
    )

    await message.reply(f"✅ Foydalanuvchi {member.full_name} tiklandi")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


# =======================
# /ban !ban (kick user)
# =======================
@group_moderator_router.message(
    IsGroup(),
    Command("ban", prefix=("!", "/")),
    IsAdmin(),
)
async def ban_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Iltimos, foydalanuvchining xabariga reply qiling!")

    member = message.reply_to_message.from_user
    member_id = member.id

    await message.chat.kick(user_id=member_id)

    await message.answer(f"✅ Foydalanuvchi {member.full_name} guruhdan haydaldi")
    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


# =======================
# /unban !unban
# =======================
@group_moderator_router.message(
    IsGroup(),
    Command("unban", prefix=("!", "/")),
    IsAdmin(),
)
async def unban_user(message: Message):
    if not message.reply_to_message:
        return await message.reply("❌ Iltimos, foydalanuvchining xabariga reply qiling!")

    member = message.reply_to_message.from_user
    member_id = member.id

    await message.chat.unban(user_id=member_id)
    await message.answer(f"✅ Foydalanuvchi {member.full_name} bandan chiqarildi")

    service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()