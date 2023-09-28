import requests

base_url = "https://vk.com/hell_yeah_xd"

def extract(base_url):
    headers = {'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0'}
    r = requests.get(url=base_url, headers=headers)
    if r.status_code != 200:
        r.raise_for_status()
    return r.text

with open('html_vk_Hell_Yeah.html', 'w', encoding='utf-8') as file:
    file.write(extract(base_url))
