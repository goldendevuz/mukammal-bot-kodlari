from aiogram.fsm.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class PersonalData(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    full_name = State()  # ism
    email = State()  # email
    phone_number = State()  # Tel raqami