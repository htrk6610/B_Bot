# handlers/veterans.py
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.veterans_menu import veterans_menu
from utils.navigation import set_menu

router = Router()


@router.message(F.text == "🪖 Ветеранам та їх родинам")
async def veterans_main(message: Message, state: FSMContext):
    await set_menu(state, "veterans")

    await message.answer(
        "Розділ для ветеранів та їх родин. Тут ви знайдете інформацію про послуги, які ми надаємо, а також корисні ресурси та контакти для підтримки.",
        reply_markup=veterans_menu
    )

@router.message(F.text == "📱 Ветеран PRO")
async def veteran_pro(message: Message):
    await message.answer(
        "Ветеран PRO — цифровий сервіс у додатку Дія.\n\n"
        "Доступні послуги:\n"
        "• єОселя\n"
        "• єВідновлення\n"
        "• субсидії\n\n"
        "Скористатись можна через додаток Дія:\n"
        "https://veteranpro.gov.ua/"
    )

@router.message(F.text == "👨‍💼 Фахівці супроводу")
async def specialists(message: Message):
    await message.answer(
        "Фахівці із супроводу ветеранів — це спеціалісти, які допомагають:\n\n"
        "• адаптація після служби\n"
        "• оформлення документів\n"
        "• отримання соціальних послуг\n\n"
        "Детальніше:\n"
        "https://mva.gov.ua/prescenter/category/86-novini/"
    )

@router.message(F.text == "📍 Де знайти фахівця")
async def find_specialist(message: Message):
    await message.answer(
        "Знайти фахівця можна за посиланням:\n\n"
        "https://mva.gov.ua/prescenter/category/86-novini/"
    )

@router.message(F.text == "📄 Надання статусів")
async def statuses(message: Message):
    await message.answer(
        "Основні статуси:\n\n"
        "• Учасник бойових дій\n"
        "• Особа з інвалідністю внаслідок війни\n"
        "• Член сім’ї загиблого\n\n"
        "Детальніше:\n"
        "https://veteranfund.com.ua/legal_consultations/status_nadanna/\n\n"
        "Через Дію:\n"
        "https://diia.gov.ua/"
    )