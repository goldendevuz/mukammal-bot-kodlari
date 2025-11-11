from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.states import PersonalData

state_router = Router()


# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, None
@state_router.message(Command("form"))
async def enter_test(message: Message, state: FSMContext):
    await message.answer("To'liq ismingizni kiriting")
    await state.set_state(PersonalData.full_name)


@state_router.message(PersonalData.full_name)
async def answer_full_name(message: Message, state: FSMContext):
    full_name = message.text

    data = await state.get_data()
    data["full_name"] = full_name
    await state.set_data(data)

    await message.answer("Emailingizni kiriting")

    await state.set_state(PersonalData.email)


@state_router.message(PersonalData.email)
async def answer_email(message: Message, state: FSMContext):
    email = message.text

    data = await state.get_data()
    data["email"] = email
    await state.set_data(data)

    await message.answer("Telefon raqam kiriting")

    await state.set_state(PersonalData.phone_number)


@state_router.message(PersonalData.phone_number)
async def answer_phone(message: Message, state: FSMContext):
    phone_number = message.text

    data = await state.get_data()
    data["phone_number"] = phone_number
    await state.set_data(data)
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    full_name = data.get("full_name")
    email = data.get("email")
    phone_number = data.get("phone_number")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ism sharifingiz - {full_name}\n"
    msg += f"Email - {email}\n"
    msg += f"Telefon: - {phone_number}"
    await message.answer(msg)

    # State dan chiqaramiz
    # 1-variant
    await state.clear()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)

    # 2 va 3 mchi variantlar Aiogramning 3-nchi versiyasida ishlamaydi!