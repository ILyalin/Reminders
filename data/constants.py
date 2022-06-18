

YEARS = ('2022', '2023','2024')

MONTHS = {}
month_name = ('Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь')
for month_number in range(len(month_name)):
    MONTHS[month_name[month_number]] = str(month_number + 1)

DAYS = tuple(str(d) for d in range(1, 32))

HOURS = tuple(str(d) for d in range(24))

MINUTES = ([str('{:02}'.format(m)) for m in range(60)])

DATE = {'YEAR': 'год', 'MONTH': 'месяц', 'DAY': 'дату', 'HOUR': 'час', 'MINUTE': 'минуту'}