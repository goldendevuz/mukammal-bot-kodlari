from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def menu_start_keyboard():
    keyboard = ReplyKeyboardBuilder()
    keyboard.row(*[KeyboardButton(text='Contact', request_contact=True)])
    keyboard.row(*[KeyboardButton(text='Location', request_location=True)])
    return keyboard.as_markup(resize_keyboard=True)