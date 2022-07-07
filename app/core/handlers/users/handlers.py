from aiogram.dispatcher import FSMContext

from data.constants import YEARS, MONTHS, DAYS, HOURS, MINUTES
from app.core.handlers.users.extra import error_in_time_keyboard
from app.core.keyboards.reply.default_keyboards import keyboard_years, keyboard_moths, keyboard_days, keyboard_hours, \
    keyboard_minutes, keyboard_make_remind
from loader import dp, types
from main import schedule_jobs
from app.core.states.params import SendMessage
from app.services.database import db


@dp.message_handler(commands=['start', 'help'])
async def send_message_welcome(message: types.Message, state: FSMContext):
    await state.finish()
    user_id = message.from_user.id
    user_name = str(message.from_user.full_name)
    await db.add_new_user(user_name,user_id)
    await message.reply(f'<b>Привет {message.from_user.first_name}</b>', reply_markup=types.ReplyKeyboardRemove())
    await message.answer('Вы можете ставить напоминания, нажав по кнопке ⬇️', reply_markup=keyboard_make_remind)
    print(message)
    print(''.join(*keyboard_make_remind['keyboard']))


@dp.message_handler(text=''.join(*keyboard_make_remind['keyboard']))
async def text_of_remind_get(message: types.Message):
    await message.answer('Введите текст напоминания:', reply_markup=types.ReplyKeyboardRemove())
    await SendMessage.waiting_for_message_of_start.set()


@dp.message_handler(state=SendMessage.waiting_for_message_of_start)
async def text_of_remind_get(message: types.Message):
    with open('text_of_message', 'w') as file_of_message:
        file_of_message.write(f"{message.from_user.id}///{message.text}")
    await SendMessage.waiting_for_text_of_reminder.set()
    await message.answer('Напоминание принято!')

    await message.answer('1️⃣ Выберите на клавиатуре год отправки:', reply_markup=keyboard_years)


@dp.message_handler(state=SendMessage.waiting_for_text_of_reminder)
async def year_of_remind_get(message: types.Message):
    if message.text not in YEARS:
        await error_in_time_keyboard(message, 'YEAR')
        return
    with open('date_time', 'w') as file_withdate:
        file_withdate.write(f'{message.text}///')
    await SendMessage.waiting_for_message_of_year.set()

    await message.answer('2️⃣ Выберите на клавиатуре месяц отправки:', reply_markup=keyboard_moths)


@dp.message_handler(state=SendMessage.waiting_for_message_of_year)
async def month_of_remind_get(message: types.Message):
    if message.text not in MONTHS:
        await error_in_time_keyboard(message, 'MONTH')
        return
    with open('date_time', 'a') as file_withdate:
        file_withdate.write(f'{message.text}///')
    await SendMessage.waiting_for_message_of_month.set()

    await message.answer('3️⃣ Выберите на клавиатуре день отправки:', reply_markup=keyboard_days)


@dp.message_handler(state=SendMessage.waiting_for_message_of_month)
async def day_of_remind_get(message: types.Message):
    if message.text not in DAYS:
        await error_in_time_keyboard(message, 'DAY')
        return
    with open('date_time', 'a') as file_withdate:
        file_withdate.write(f'{message.text}///')
    await SendMessage.waiting_for_message_of_day.set()

    await message.answer('4️⃣ Выберите на клавиатуре час отправки:', reply_markup=keyboard_hours)


@dp.message_handler(state=SendMessage.waiting_for_message_of_day)
async def hour_of_remind_get(message: types.Message):
    if message.text not in HOURS:
        await error_in_time_keyboard((message, 'HOUR'))
        return
    with open('date_time', 'a') as file_withdate:
        file_withdate.write(f'{message.text}///')
    await SendMessage.waiting_for_message_of_hour.set()

    await message.answer('5️⃣ Выберите на клавиатуре минуту отправки:', reply_markup=keyboard_minutes)


@dp.message_handler(state=SendMessage.waiting_for_message_of_hour)
async def minutes_of_remind_get(message: types.Message, state=FSMContext):
    if message.text not in MINUTES:
        await error_in_time_keyboard((message, 'MINUTE'))
        return
    with open('date_time', 'a') as file_withdate:
        file_withdate.write(f'{message.text}///')
        await message.reply('Напоминание поставлено!', reply_markup=keyboard_make_remind)
    schedule_jobs()
    with open('date_time', 'r') as inFile:
        date_data = inFile.read().split("///")
        print(date_data)
        print(int(date_data[0]), int(MONTHS[str(date_data[1])]), int(date_data[2]), int(date_data[3]),
              int(date_data[4]))
        await message.reply(f'1️⃣ <b>Год</b>: {date_data[0]}\n'
                            f'2️⃣️ <b>Месяц</b>: {date_data[1]}\n'
                            f'3️⃣ <b>День</b>: {date_data[2]}\n'
                            f'4️⃣ <b>Время</b>: <u>{date_data[3]}:{date_data[4]}</u>')
    await state.finish()
