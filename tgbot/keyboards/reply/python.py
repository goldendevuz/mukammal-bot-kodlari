from itertools import chain

from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_python_keyboard():
    keyboard = ReplyKeyboardBuilder()
    buttons = [
        ["#00 Kirish", "#01 Kerarkli dasturlar", "#02 Hello World!"],
        ["Ortga", "Boshiga"],
    ]
    keyboard.row(*[KeyboardButton(text=i) for i in chain(*buttons)])
    return keyboard.as_markup(resize_keyboard=True)