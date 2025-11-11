from aiogram import types, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.formatting import Bold, Text, Italic, Underline, Strikethrough, TextLink, Code

info_router = Router()


@info_router.message(Command('info'))
async def bot_info(message: types.Message):
    content = Text(
        f"Assalom alaykum, {message.from_user.full_name}\n",
        "Bu ", Bold('qalin matn.\n'),
        "Bu esa ", Italic('egri matn.\n'),
        "Bu ", Underline('ostiga chizilgan matn.\n'),
        "Bu esa ", Strikethrough("o'chirilgan matn.\n"),
        "Bu esa ", TextLink('Mohirdev sahifasiga link\n', url='https://mohirdev.uz'),
        "Bu esa ", Code('print("Hello World!")') + " kod\n",
    )
    await message.reply(**content.as_kwargs())


@info_router.message(Command('info_html'))
async def bot_info(message: types.Message):
    text = f"Assalom alaykum, {message.from_user.full_name}!\n"
    text += "Bu <b>qalin matn.</b>\n"
    text += "Bu esa <i>egri matn.</i>\n"
    text += "Bu <u>ostiga chizilgan matn.</u>\n"
    text += "Bu esa <s>o'chirilgan matn.</s>\n"
    text += "Bu esa <a href='https://mohirdev.uz'>Mohirdev sahifasiga link</a>.\n"
    text += "Bu esa <code>print('Hello World!')</code> kod.\n"

    await message.reply(text, parse_mode=ParseMode.HTML)


@info_router.message(Command('info_markdown'))
async def bot_info(message: types.Message):
    text = f"Assalom alaykum, {message.from_user.full_name}\!\n"
    text += "Bu *qalin matn\.*\n"
    text += "Bu esa _egri matn_\n"
    text += "Bu __ostiga chizilgan matn__\n"
    text += "Bu esa ~o'chirilgan matn~\n"
    text += "Bu esa [Mohirdev sahifasiga link](https://mohirdev.uz)\n"
    text += "Bu esa `print('Hello World!')` kod\n"

    await message.reply(text, parse_mode=ParseMode.MARKDOWN_V2)