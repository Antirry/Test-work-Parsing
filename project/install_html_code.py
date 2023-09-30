import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://vk.com/hell_yeah_xd")

for _ in range(6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)

with open('html_vk_Hell_Yeah.html', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)

driver.close()
