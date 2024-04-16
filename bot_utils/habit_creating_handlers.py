from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext

from .FSM import FSM_CreteNewHabit


storage = MemoryStorage()


async def take_habit_title_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit title
    """
    await message.answer("Введи название привычки")
    await state.set_state(FSM_CreteNewHabit.habit_description)


async def take_habit_description_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit description
    """
    storage.update_data(habit_title=message.text)
    await message.answer("Введи описание привычки")
    await state.set_state(FSM_CreteNewHabit.habit_act_time)


async def take_habit_act_time_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit act time
    """
    storage.update_data(habit_description=message.text)
    await message.answer("Во сколько нужно выполнить привычку?\nВведи дату в формате ЧЧ:ММ")
    await state.set_state(FSM_CreteNewHabit.chose_award_or_habit)


async def choose_award_or_habit(message: Message, state: FSMContext) -> None:
    storage.update_data(act_time=message.text)

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text="Награда"), KeyboardButton(text="Привычка"))
    await state.set_state(FSM_CreteNewHabit.chose_award_or_habit)

    await message.answer("Выбери: награда, или привычка?")
    

async def take_habit_award_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit award
    """
    await state.set_state(FSM_CreteNewHabit.habit_award)
    storage.update_data(act_time=message.text)
    await message.answer("Enter habit award")


async def take_habit_useful_habit_handler(message: Message, state: FSMContext) -> None:
    """
    Handler will take habit useful habit
    """
    await state.set_state(FSM_CreteNewHabit.habit_useful_habit)
    storage.update_data(act_time=message.text)
    await message.answer("Enter habit useful habit")
