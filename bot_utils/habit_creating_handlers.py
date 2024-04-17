from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from .FSM import FSM_CreteNewHabit, FSM_CreateAward, FSM_CreateUsefulHabit
from bot_texts import keyboard_texts as kb
from bot_texts import text_messages as txt


storage = MemoryStorage()


async def take_habit_description_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit description
    """
    await state.update_data(habit_title=message.text)
    await message.answer("Введи описание привычки")
    await state.set_state(FSM_CreteNewHabit.habit_act_time)


async def take_habit_act_time_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit act time
    """
    await state.update_data(habit_description=message.text)
    await message.answer("Во сколько нужно выполнить привычку?\nВведи дату в формате ЧЧ:ММ")
    await state.set_state(FSM_CreteNewHabit.chose_award_or_habit)


async def choose_award_or_habit(message: Message, state: FSMContext) -> None:
    await state.update_data(act_time=message.text)
    award_button, habit_button = KeyboardButton(text=kb.award_text), KeyboardButton(text=kb.habit_text)

    keyboard = ReplyKeyboardMarkup(
        keyboard=[[award_button, habit_button]], 
        resize_keyboard=True
    )
    await state.set_state(FSM_CreteNewHabit.wait_for_deciding)
    await message.answer(txt.habit_or_award, reply_markup=keyboard)    


async def take_users_answer(message: Message, state: FSMContext) -> None:
    
    data = await state.get_data()
    await message.answer(text=f"{data}")
    match message.text:
        case kb.award_text:
            await state.set_state(FSM_CreateAward.award_title)
            await message.answer("Ты выбрал награду.\nТы хочешь создать ее, или выбрать существующую?")
        
        case kb.habit_text:
            await state.set_state(FSM_CreateUsefulHabit.useful_habit_title)
            await message.answer("Ты выбрал привычку.\nТы хочешь создать ее, или выбрать существующую?")
    await state.clear()


async def take_habit_award_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit award
    """
    await state.set_state(FSM_CreteNewHabit.habit_award)
    await message.answer("Enter habit award")


async def take_habit_useful_habit_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit useful habit
    """
    await state.set_state(FSM_CreteNewHabit.habit_useful_habit)
    await message.answer("Enter habit useful habit")
