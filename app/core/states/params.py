from aiogram.dispatcher.filters.state import State, StatesGroup


class SendMessage(StatesGroup):
    waiting_for_message_of_start = State()
    waiting_for_text_of_reminder = State()
    waiting_for_message_of_year = State()
    waiting_for_message_of_month = State()
    waiting_for_message_of_day = State()
    waiting_for_message_of_hour = State()
    waiting_for_message_of_minute = State()
