from data.constants import DATE, MONTHS
from loader import types


async def error_in_time_keyboard(message: types.Message, time_of_one_position_in_date):

    await message.answer(f'Пожалуйста выберите {DATE[time_of_one_position_in_date]} на клавиатуре')


def extra_days_based_on_month():
    nums_of_month_with_31days = ('1', '3', '5', '7', '8', '10', '12')
    with open('date_time', 'r') as file_withdate:
        num_of_month = MONTHS[file_withdate.read().split('///')[1]]
        if num_of_month in nums_of_month_with_31days:
            return 0
        elif num_of_month not in nums_of_month_with_31days and num_of_month != '2':
            return 1
        else:
            return 3
