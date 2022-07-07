from datetime import datetime

from loader import scheduler


def get_actual_date():
    date_and_time_now = datetime.now()
    minute_now = date_and_time_now.minute
    hour_now = date_and_time_now.hour
    day_now = date_and_time_now.day
    month_now = date_and_time_now.month
    year_now = date_and_time_now.year

    print(minute_now, hour_now, day_now, month_now, year_now)


def schedule_job_for_get_update():
    scheduler.add_job(get_actual_date, 'interval', seconds=10)
