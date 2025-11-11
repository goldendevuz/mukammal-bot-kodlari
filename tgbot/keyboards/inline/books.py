from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .common import back_button
from .callback_data import BookCallback

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash. JavaScript": "js_book",
}

# Build inline keyboard list manually
book_buttons = [
    [InlineKeyboardButton(text=title, callback_data=BookCallback(item_name=value).pack())]
    for title, value in books.items()
]

# Add back button in a new row
book_buttons.append([back_button])

# Create markup
booksMenu = InlineKeyboardMarkup(inline_keyboard=book_buttons)