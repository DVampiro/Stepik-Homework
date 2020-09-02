from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import pyperclip


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
with webdriver.Chrome() as browser:
    browser.get(link)
    browser.implicitly_wait(5)

    text = WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    browser.find_element_by_class_name("btn").click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    a_element = browser.find_element_by_id('answer')
    a_element.send_keys(str(y))
    browser.find_element_by_id('solve').click()

    answer = browser.switch_to.alert.text.split()[-1]
    pyperclip.copy(answer)

    print('Ответ:', answer)
