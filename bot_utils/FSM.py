from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


class FSM_CreteNewHabit(StatesGroup):
    habit_title = State()
    habit_description = State()
    habit_act_time = State()
    chose_award_or_habit = State()
    habit_award = State()
    habit_useful_habit = State()


storage = MemoryStorage()