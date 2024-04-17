from aiogram import html
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from aiogram import types as t
from bot_texts import keyboard_texts as kb
from bot_texts import text_messages as txt
from bot_utils.FSM import FSM_CreteNewHabit

import requests

storage = MemoryStorage()


async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")
    try:
        data = {
            "user_id": message.from_user.id,
            "name": message.from_user.full_name,
            "username": message.from_user.username
        }
        response = requests.post("http://localhost:8000/users/register_user/", json=data)
        if response.status_code in {200, 201}:
            await message.answer(txt.registered_message)
        else:
            await message.answer(txt.logging_in_message)
        
        create_new_habit_button = t.KeyboardButton(text=kb.create_new_habit_text)
        check_my_habits_button = t.KeyboardButton(text=kb.check_my_habits_text)
        view_all_habits_button = t.KeyboardButton(text=kb.view_all_habits_text)
        
        # Создание клавиатуры новым для меня методом. Раньше было не так
        start_keyboard = t.ReplyKeyboardMarkup(
            keyboard=[
                [create_new_habit_button, check_my_habits_button],
                [view_all_habits_button]
            ], 
            resize_keyboard=True
        )

        await message.answer(txt.start_button_kb, reply_markup=start_keyboard)

    except Exception as e:
        print(e)
        await message.answer(txt.access_denied_message)


# ? Создание новой привычки
async def create_new_habit_handler(message: Message, state: FSMContext) -> None:    
    await message.answer("Давай начнем создание привычки!\nКак назвать новую привычку?", reply_markup=t.ReplyKeyboardRemove())
    await state.set_state(FSM_CreteNewHabit.habit_description)


async def watch_my_habits_handler(message: Message) -> None:
    """
    Handler will check my habits
    """
    await message.answer("Check my habits TEST")


async def view_all_habits_handler(message: Message) -> None:
    """
    Handler will view all habits
    """
    await message.answer("View all habits TEST")