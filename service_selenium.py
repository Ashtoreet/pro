import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver

import time

# html = 'https://service.nalog.ru/uwsfind.do'
# html = 'https://service.nalog.ru/bi.do'
inn = [7, 7, 1, 8, 6, 0, 3, 1, 5, 0]
driver = webdriver.Chrome()
html = 'https://service.nalog.ru/zd.do'


driver.get(html)
driver.implicitly_wait(15) # это таймер

# тут работает ввод инн из переменной
input_inn = driver.find_element_by_id('inn')
for i in inn:
    driver.implicitly_wait(5)
    input_inn.send_keys(i)

# s = get_soup(html)
# capcha(s)
img_url = driver.find_element_by_tag_name('img').get_attribute('src')
responce = requests.get(img_url)
img = Image.open(BytesIO(responce.content))
img.show()

# тут работает ввод капчи с консоли
user_input = input('Enter captcha -> ', )
list_user_input = list(map(int,"".join(map(str, user_input))))
input_captcha = driver.find_element_by_id('captcha')

for c in list_user_input:
    driver.implicitly_wait(4)
    input_captcha.send_keys(c)


button = driver.find_element_by_id('btn_send')
print('нажали', button.click())
# driver.implicitly_wait(40)
time.sleep(5)

value = driver.find_element_by_id('resultData').text.strip()
msg = driver.find_element_by_id('resultData').get_attribute('outerHTML')

if value:
    print(value)
else:
    print('пусто', msg)

driver.close()
