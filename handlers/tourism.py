from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from keyboards.tourism_menu import tourism_menu
from utils.navigation import set_menu

router = Router()


@router.message(F.text == "🗺 Туризм")
async def tourism_main(message: Message, state: FSMContext):
    await set_menu(state, "tourism")

    await message.answer(
        "Туристичні можливості Бучанського району",
        reply_markup=tourism_menu
    )


@router.message(F.text == "🌳 Туристичні місця")
async def tourism_places(message: Message):
    await message.answer(
        "Бучанський район запрошує туристів відправитися у насичену мандрівку.\n\n"
        "Тут є багато різноманітних пам‘яток та парків, де можна провести незабутньо час "
        "та відволіктися від цивілізації.\n\n"
        "Музеї, парки, заповідники, урочища, площі — та це тільки початок.\n\n"
        "Детальніше:\n"
        "https://kyivregiontours.gov.ua/places?rd=bucha-district"
    )

@router.message(F.text == "🕯 Маршрут пам'яті")
async def memory_route(message: Message):
    await message.answer(
        "Щоб пам'ять не згасала — створено маршрут пам'яті місцями подій "
        "лютого–березня 2022 року.\n\n"
        "Ознайомитися можна тут:\n"
        "https://kyivregiontours.gov.ua/memory/"
    )