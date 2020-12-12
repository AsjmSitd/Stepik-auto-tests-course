"""Задание на execute_script
В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером, который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit"."""
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    y = calc(x_element.text)

    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()