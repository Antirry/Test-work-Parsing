import locale
import re
from datetime import datetime

# Set the locale to Russian
locale.setlocale(locale.LC_TIME, 'ru_RU')


def to_full_date(date_str: str) -> str:
    symbols = "".join(re.findall(r'[а-я]', date_str))

    month = symbols[:3]

    return date_str.replace(symbols, 'май') if month == 'мая' else date_str.replace(symbols, month)

def convert_to_date(date_list_string: list[str]) -> tuple[datetime.date]:

    date_list = []

    for i in date_list_string:
        i = i.replace('\xa0', '')
        try:
            date = datetime.strptime(to_full_date(i), '%d%b%Y').date()
            date_list.append(date)
        except ValueError:
            try:
                i = i.rsplit('в', 1)
                date = to_full_date(i[0]) + str(datetime.now().year)
                date = datetime.strptime(date, '%d%b%Y').date()
                date_list.append(date)
            except ValueError:
                date = datetime.now().date()
                date_list.append(date)

    return date_list


def extract_views(s:str):
    return re.search(r'\d+', s).group()
