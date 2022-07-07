import logging
import datetime

from aiogram import executor
from datetime import datetime

from data.constants import MONTHS
from loader import bot, scheduler

from get_date_update import schedule_job_for_get_update

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


async def send_message_by_timer():
    with open('text_of_message', 'r') as text_in_File:
        file_content = text_in_File.read().split("///")
        user_id, text = int(file_content[0]), file_content[1]
        await bot.send_message(chat_id=user_id, text=text)


def schedule_jobs():
    with open('date_time', 'r') as inFile:
        date_data = inFile.read().split("///")
        scheduler.add_job(send_message_by_timer, 'date',
                          run_date=datetime(int(date_data[0]), int(MONTHS[str(date_data[1])]), int(date_data[2]),
                                            int(date_data[3]),
                                            int(date_data[4])))


if __name__ == '__main__':
    from app.core.handlers import dp
    schedule_job_for_get_update()
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)
