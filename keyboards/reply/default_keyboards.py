from data.constants import YEARS, MONTHS, DAYS, HOURS, MINUTES
from loader import types
from keyboards.reply.keyboard_formatting import three_line_keyboard_generation

keyboard_years = types.ReplyKeyboardMarkup(
    keyboard=[
    ],
    resize_keyboard=True
)
three_line_keyboard_generation(keyboard_years, YEARS)

keyboard_moths = types.ReplyKeyboardMarkup(
    keyboard=[

    ],
    resize_keyboard=True
)
three_line_keyboard_generation(keyboard_moths, MONTHS)

keyboard_days = types.ReplyKeyboardMarkup(
    keyboard=[

    ],
    resize_keyboard=True)
three_line_keyboard_generation(keyboard_days, DAYS)

keyboard_hours = types.ReplyKeyboardMarkup(
    keyboard=[
    ],
    resize_keyboard=True)
three_line_keyboard_generation(keyboard_hours, HOURS)

keyboard_minutes = types.ReplyKeyboardMarkup(
    keyboard=[

    ],
    resize_keyboard=True)
three_line_keyboard_generation(keyboard_minutes,MINUTES)

keyboard_make_remind = types.ReplyKeyboardMarkup(resize_keyboard=True).add('Поставить напоминание ✅')
