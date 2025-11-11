from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .common import back_button
from .callback_data import CourseCallback

# Define your buttons (each row = list)
buttons = [
    [
        InlineKeyboardButton(
            text="🐍 Python Dasturlash Asoslari",
            callback_data=CourseCallback(item_name="python").pack()
        )
    ],
    [
        InlineKeyboardButton(
            text="🌐 Django Web Dasturlash",
            callback_data=CourseCallback(item_name="django").pack()
        )
    ],
    [
        InlineKeyboardButton(
            text="🤖 Mukammal Telegram bot",
            callback_data="course:telegram"
        )
    ],
    [
        InlineKeyboardButton(
            text="📈 Ma'lumotlar Tuzilmasi va Algoritmlar",
            callback_data="course:algorithm"
        )
    ],
    [back_button],
]

# Create markup
coursesMenu = InlineKeyboardMarkup(inline_keyboard=buttons)