from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands_list = [
        ["start", "Launch the bot"],
        ["set_photo", "Guruh rasmini o'zgartirish"],
        ["set_title", "Guruh nomini o'zgartirish"],
        ["set_description", "Guruh haqidagi ma'lumotni o'zgartirish"],
        ["ro", "Foydalanuvchini Read Only (RO) rejimga o'tkazish"],
        ["unro", "RO rejimdan chiqarish"],
        ["ban", "Ban"],
        ["unban", "Bandan chiqarish"],
    ]
    commands = [
        BotCommand(
            command=command[0],
            description=command[1] if len(command) == 2 else command[0],
        ) for command in commands_list
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())