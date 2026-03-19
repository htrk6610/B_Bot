from aiogram.fsm.context import FSMContext


async def set_menu(state: FSMContext, menu: str):
    data = await state.get_data()
    stack = data.get("menu_stack", [])

    stack.append(menu)

    await state.update_data(menu_stack=stack)


async def back(state: FSMContext):
    data = await state.get_data()
    stack = data.get("menu_stack", [])

    if len(stack) > 1:
        stack.pop()

    await state.update_data(menu_stack=stack)

    return stack[-1] if stack else "main"