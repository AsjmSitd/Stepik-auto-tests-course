"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание."""
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button1 = browser.find_element_by_class_name('btn.btn-primary')
    button1.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_element = browser.find_element_by_id("input_value")
    y = calc(x_element.text)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button2 = browser.find_element_by_class_name('btn.btn-primary')
    button2.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
    
