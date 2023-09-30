from bs4 import BeautifulSoup
from convert import convert_to_date, extract_views

HTMLFILE = open('html_vk_Hell_Yeah.html', 'r', encoding='utf-8').read()

s = BeautifulSoup(HTMLFILE, 'html.parser')

def extract_text(list_html: list) -> list:
    list_elements = []

    for i in list_html:
        list_elements.append(i.text.replace(' ', ''))

    return list_elements


likes = extract_text(
    s.find_all('div',
               class_="PostButtonReactions__title _counter_anim_container")
)
likes = tuple(map(int, likes))

time_posts = extract_text(s.find_all('time', class_="PostHeaderSubtitle__item"))
time = convert_to_date(time_posts)

views = (int(extract_views(i.get('title')))
         for i in s.find_all('div', class_="like_views like_views--inActionPanel"))

shared_posts = extract_text(
    s.find_all('span',
        class_="PostBottomAction__count _like_button_count _counter_anim_container PostBottomAction__count--withBg")[1::2]
)
shared = tuple(map(int, shared_posts))
