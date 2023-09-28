from bs4 import BeautifulSoup
from convert_date import convert_to_date

HTMLFILE = open('html_vk_Hell_Yeah.html', 'r', encoding='utf-8').read()

s = BeautifulSoup(HTMLFILE, 'html.parser')

def extract_text(list_html: list) -> list:
    list_elements = []

    for i in list_html:
        list_elements.append(i.text)

    return list_elements

def to_thousand_views(views_str:list[str]) -> list[int]:
    views = tuple(
                int(views.rstrip('K')) * 1000
                if 'K' in views else int(views)
                for views in views_str
    )

    return views



likes_posts = extract_text(
    s.find_all('div',
               class_="PostButtonReactions__title _counter_anim_container")
)

likes = tuple(map(int, likes_posts))

time_posts = extract_text(s.find_all('time', class_="PostHeaderSubtitle__item"))
time = convert_to_date(time_posts)

views_posts = extract_text(s.find_all('span', class_="_views"))
views = to_thousand_views(views_posts)

shared_posts = extract_text(
    s.find_all('span',
        class_="PostBottomAction__count _like_button_count _counter_anim_container PostBottomAction__count--withBg")
)
shared = tuple(map(int, shared_posts))[:len(time)]
