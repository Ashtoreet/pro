import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver

import time

# html = 'https://service.nalog.ru/uwsfind.do'
# html = 'https://service.nalog.ru/bi.do'
inn = # [*, *, *, *, *, *, *, *, *, *]
driver = webdriver.Chrome()
html = 'https://service.nalog.ru/zd.do'


def input_inn_to_form(driver, inn):
    """ Input inn from variable. """
    input_inn = driver.find_element_by_id('inn') # find inn form

    for i in inn:
        driver.implicitly_wait(5) # timer
        input_inn.send_keys(i) # input one by one


def open_img(driver):
    """ Open image. """
    img_url = driver.find_element_by_tag_name('img').get_attribute('src')
    responce = requests.get(img_url)
    img = Image.open(BytesIO(responce.content))
    img.show()

def enter_cap(driver):
    """ тут работает ввод капчи с консоли """
    user_input = input('Enter captcha -> ', ) # get numbers
    list_user_input = list(map(int,"".join(map(str, user_input)))) # turn to list
    input_captcha = driver.find_element_by_id('captcha') # find form

    for c in list_user_input:
        driver.implicitly_wait(4) #timer
        input_captcha.send_keys(c) # input one by one


def click_button(driver):
    button = driver.find_element_by_id('btn_send')
    print('нажали', button.click())


def getting_output(driver):
    value = driver.find_element_by_id('resultData').text.strip()
    msg = driver.find_element_by_id('resultData').get_attribute('outerHTML')

    if value:
        print(value)
    else:
        print('пусто', msg)


if __name__ == '__main__':
    driver.get(html)
    driver.implicitly_wait(15) # это таймер

    input_inn_to_form(driver, inn)
    open_img(driver)
    enter_cap(driver)
    click_button(driver)

    time.sleep(5)

    getting_output(driver)
    driver.close()
