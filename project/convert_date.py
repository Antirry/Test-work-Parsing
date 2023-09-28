import locale
import re
from datetime import datetime

# Set the locale to Russian
locale.setlocale(locale.LC_TIME, 'ru_RU')

def to_full_date(date_str: str) -> str:
    months = ('Январь', 'Февраль', 'Март',
              'Апрель', 'Май', 'Июнь',
              'Июль', 'Август', 'Сентябрь',
              'Октябрь', 'Ноябрь', 'Декабрь'
    )

    months_short = tuple(
        'мая' if x[:3].lower() == 'май' else x[:3].lower() for x in months)

    date_str_filtered = re.sub(r'(\d+)\s+(\w{3})',
        lambda match:
          match.group(1) + ' ' + months[months_short.index(match.group(2))], date_str)

    return date_str_filtered

def convert_to_date(date_list_string: list[str]) -> tuple[datetime.date]:

    date_list = []

    for i in date_list_string:
        if 'в' not in i:
            date = datetime.strptime(i, '%d %b %Y').date()
            date_list.append(date)

        elif ' в ' in i:
            i = i.split('в')
            date = to_full_date(i[0]) + str(datetime.now().year)

            date = datetime.strptime(date, '%d %B %Y').date()
            date_list.append(date)

        else:
            date = datetime.now().date
            date_list.append(date)

    return tuple(date_list)
