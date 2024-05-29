from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from .FSM import FSM_CreteNewHabit

from bot_texts import text_messages as txt
from bot_texts import keyboard_texts as kb
from bot_utils import keyboards as kbs

import re


state = MemoryStorage()


async def take_habit_title_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit title
    """
    await state.update_data(habit_title=message.text)
        
    await message.answer(txt.new_habit_description, reply_markup=ReplyKeyboardRemove())
    await state.set_state(FSM_CreteNewHabit.habit_description)


async def take_habit_description_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit description
    """
    await state.update_data(habit_description=message.text) # Запись данных в хранилище
    await message.answer(txt.new_habit_act_time)
    await state.set_state(FSM_CreteNewHabit.habit_act_time)


async def take_habit_act_time_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit act time
    """
    print(f"[LOG] Присланное сообщение {message.text}")
    if not re.match(r"[0-2]\d:[0-5]\d", message.text):
        print('[LOG] Неправильный формат времени')
        await state.set_state(FSM_CreteNewHabit.invalid_time_format)
        await message.answer(txt.invalid_time_format)
        return

    print('[LOG] Пытаюсь выставить клавиатуру')
    await state.update_data(habit_act_time=message.text)
    habit_button = KeyboardButton(text=kb.useful_habit_button)
    award_button = KeyboardButton(text=kb.award_button)
    keyboard = ReplyKeyboardMarkup(keyboard=[[habit_button, award_button]], resize_keyboard=True)
    
    await state.set_state(FSM_CreteNewHabit.choose_award_or_habit)
    await message.answer(txt.new_habit_choose_award_or_habit, reply_markup=keyboard)


async def invalid_time_format_handler(message: Message, state: FSMContext) -> None:
    """Функция-валидатор ввода времени в формате ЧЧ:ММ"""
    print('[LOG] Отправляю обратно в состояние FSM_CreteNewHabit.habit_act_time')    
    await state.set_state(FSM_CreteNewHabit.habit_act_time)    
    await message.answer(txt.invalid_time_format)
    return
    

async def choose_award_or_habit(message: Message, state: FSMContext) -> None:
    await state.update_data(award_or_habit=message.text)
# ? Костыльная валидация выбора кнопки. 
    while True:
        if message.text == kb.useful_habit_button:
            await message.answer(txt.choose_useful_habit, reply_markup=kbs.habits_keyboard)
            await state.set_state(FSM_CreteNewHabit.habit_useful_habit)
            break
        elif message.text == kb.award_button:
            await message.answer(txt.new_habit_award, reply_markup=kbs.awards_keyboard)
            await state.set_state(FSM_CreteNewHabit.habit_award)
            break
        else:
            await message.answer(txt.invalid_input, reply_markup=ReplyKeyboardRemove())

# * Хендлеры для работы с привычками
async def take_habit_handler(message: Message, state: FSMContext) -> None:
    """
    Хендлер для работы с привычками
    """
    await state.update_data(act_time=message.text)
    await message.answer(text=txt.choose_useful_habit)
    


async def take_habit_useful_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit useful habit
    """
    await state.update_data(act_time=message.text)
    await message.answer(text=txt.choose_award)
    
