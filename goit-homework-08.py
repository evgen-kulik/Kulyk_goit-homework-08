from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    """Виводить список іменинників"""

    global near_saturday, last_sunday
    current_datetime = datetime.now()  # Поточна дата з часом.
    current_date = current_datetime.date()  # Поточна дата без часу. 2023-04-13
    print(f'Поточна дата: {current_date}')
    number_day = current_datetime.weekday()  # Номер дня тижня (дні тижня у Python починаються з понеділка і він = 0).

    # Розрахуємо дату найближчої суботи та крайньої правої неділі
    if number_day == 0:
        near_saturday = current_date + timedelta(days=5)
        last_sunday = current_date + timedelta(days=13)
    elif number_day == 1:
        near_saturday = current_date + timedelta(days=4)
        last_sunday = current_date + timedelta(days=12)
    elif number_day == 2:
        near_saturday = current_date + timedelta(days=3)
        last_sunday = current_date + timedelta(days=11)
    elif number_day == 3:
        near_saturday = current_date + timedelta(days=2)
        last_sunday = current_date + timedelta(days=10)
    elif number_day == 4:
        near_saturday = current_date + timedelta(days=1)
        last_sunday = current_date + timedelta(days=9)
    elif number_day == 5:
        near_saturday = current_date
        last_sunday = current_date + timedelta(days=8)
    elif number_day == 6:
        near_saturday = current_date - timedelta(days=1)
        last_sunday = current_date + timedelta(days=7)
    print(f'Найближча субота: {near_saturday}')
    print(f'Крайня права неділя: {last_sunday}')

    # Відсортуємо із загального списку словників дати, які знаходяться в інтервалі між
    # ближчою суботою і крайньою правою неділею.
    lst_dates = []
    for i in users:
        if near_saturday.month <= i['birthday'].month <= last_sunday.month and \
                near_saturday.day <= i['birthday'].day <= last_sunday.day:
            lst_dates.append(i)
    # print(lst_dates)

    # Визначимо репери дат для подальшого сортування.
    monday = near_saturday + timedelta(days=2)  # У понеділок вітаємо того, хто народився в період субота-понеділок.
    tuesday = near_saturday + timedelta(days=3)
    wednesday = near_saturday + timedelta(days=4)
    thursday = near_saturday + timedelta(days=5)
    friday = near_saturday + timedelta(days=6)
    saturday = near_saturday + timedelta(days=7)
    sunday = near_saturday + timedelta(days=8)

    # Створимо списки по днях тижня для наповнення іменами.
    lst_monday = []
    lst_tuesday = []
    lst_wednesday = []
    lst_thursday = []
    lst_friday = []
    lst_saturday = []
    lst_sunday = []

    # Наповнимо списки іменами
    for i in lst_dates:
        if near_saturday.day <= i['birthday'].day <= monday.day:
            lst_monday.append(i['name'])
        if tuesday.day == i['birthday'].day:
            lst_tuesday.append(i['name'])
        if wednesday.day == i['birthday'].day:
            lst_wednesday.append(i['name'])
        if thursday.day == i['birthday'].day:
            lst_thursday.append(i['name'])
        if friday.day == i['birthday'].day:
            lst_friday.append(i['name'])
        if saturday.day == i['birthday'].day:
            lst_saturday.append(i['name'])
        if sunday.day == i['birthday'].day:
            lst_sunday.append(i['name'])

    # Виведемо результати
    if len(lst_monday) > 0:
        print(f'Monday: {", ".join(lst_monday)}')
    if len(lst_tuesday) > 0:
        print(f'Tuesday: {", ".join(lst_tuesday)}')
    if len(lst_wednesday) > 0:
        print(f'Wednesday: {", ".join(lst_wednesday)}')
    if len(lst_thursday) > 0:
        print(f'Thursday: {", ".join(lst_thursday)}')
    if len(lst_friday) > 0:
        print(f'Friday: {", ".join(lst_friday)}')
    if len(lst_saturday) > 0:
        print(f'Saturday: {", ".join(lst_saturday)}')
    if len(lst_sunday) > 0:
        print(f'Sunday: {", ".join(lst_sunday)}')


users = [
    {'name': 'минула субота', 'birthday': datetime(year=1980, month=4, day=15)},
    {'name': 'минула неділя', 'birthday': datetime(year=1985, month=4, day=16)},
    {'name': 'понеділок', 'birthday': datetime(year=1990, month=4, day=17)},
    {'name': 'вівторок', 'birthday': datetime(year=1992, month=4, day=18)},
    {'name': 'середа', 'birthday': datetime(year=1992, month=4, day=19)},
    {'name': 'четвер', 'birthday': datetime(year=1992, month=4, day=20)},
    {'name': "п'ятниця", 'birthday': datetime(year=1992, month=4, day=21)},
    {'name': 'субота', 'birthday': datetime(year=1992, month=4, day=22)},
    {'name': 'неділя', 'birthday': datetime(year=1992, month=4, day=23)},
    {'name': 'неділя_2', 'birthday': datetime(year=1992, month=4, day=23)},
    {'name': 'неділя_3', 'birthday': datetime(year=1992, month=4, day=23)}
]

get_birthdays_per_week(users)

