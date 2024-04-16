import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from bot_utils.FSM import FSM_CreteNewHabit
from bot_utils.handlers import storage

from bot_texts import keyboard_texts as kb
from bot_utils import handlers
from bot_utils import habit_creating_handlers as hch


dp = Dispatcher(storage=storage)

# * Хендлеры
dp.message.register(handlers.command_start_handler, CommandStart()) # ? Хендлер для стартовой команды

dp.message.register(handlers.create_new_habit_handler, F.text == kb.create_new_habit_text) # ? Хендлер создания новой привычки
dp.message.register(hch.take_habit_title_handler, StateFilter(dp, FSM_CreteNewHabit.habit_title), F.text) # *Название привычки
dp.message.register(hch.take_habit_description_handler, StateFilter(dp, FSM_CreteNewHabit.habit_description), F.text) # *Описание привычки
dp.message.register(hch.take_habit_act_time_handler, StateFilter(dp, FSM_CreteNewHabit.habit_act_time), F.text) # *Время выполнения привычки

dp.message.register(handlers.watch_my_habits_handler, F.text == kb.check_my_habits_text) # ? Хендлер просмотра моих привычек
dp.message.register(handlers.view_all_habits_handler, F.text == kb.view_all_habits_text) # ? Хендлер просмотра привычек всех пользователей


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=getenv("BOT_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
