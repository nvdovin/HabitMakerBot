from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


class FSM_CreteNewHabit(StatesGroup):
    habit_title = State()
    habit_description = State()
    habit_act_time = State()
    choose_award_or_habit = State()
    habit_award = State()
    habit_useful_habit = State()
    invalid_time_format = State()


class FSM_UsefulHabit(StatesGroup):
    useful_habit = State()


storage = MemoryStorage()