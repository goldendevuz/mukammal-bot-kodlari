from aiogram.filters.callback_data import CallbackData

class CourseCallback(CallbackData, prefix="course"):
    item_name: str

class BookCallback(CallbackData, prefix="book"):
    item_name: str