from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


class FSM_CreteNewHabit(StatesGroup):
    habit_title = State()
    habit_description = State()
    habit_act_time = State()
    chose_award_or_habit = State()
    wait_for_deciding = State()
    habit_send_data = State()


class FSM_CreateUsefulHabit(StatesGroup):
    useful_habit_title = State()
    useful_habit_description = State()
    useful_habit_send_data = State()


class FSM_CreateAward(StatesGroup):
    award_title = State()
    award_description = State()
    award_send_data = State()


storage = MemoryStorage()