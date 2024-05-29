from aiogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from bot_texts import keyboard_texts as kb

# ? Главное меню
main_menu_button = KeyboardButton(text=kb.main_menu_button)

# ? Работа с полезными привычками
create_new_habit_button = KeyboardButton(text=kb.create_new_habit_button)
check_my_habits_button = KeyboardButton(text=kb.view_all_my_habits_button)
view_all_habits_button = KeyboardButton(text=kb.view_all_habits)

# ? Работа с наградами
create_new_award_button = KeyboardButton(text=kb.create_new_award_button)
view_all_my_awards_button = KeyboardButton(text=kb.view_all_my_awards_button)
view_all_awards_button = KeyboardButton(text=kb.view_all_awards)


# ? Клавиатуры

# ? Для работы с привычками
habits_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            create_new_habit_button, 
            check_my_habits_button,
        ],
        [
            view_all_habits_button, 
            main_menu_button
        ]
    ], 
    resize_keyboard=True
)

# ? Для работы с наградами
awards_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            create_new_award_button, 
            view_all_my_awards_button,
        ],
        [
            main_menu_button,
            view_all_awards_button
        ]    
    ], 
    resize_keyboard=True
)