"""Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание."""

from selenium import webdriver
import math
import time

browser = webdriver.Chrome()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    #time.sleep(2)
    current_window = browser.current_window_handle
    browser.switch_to.window(current_window)
    button1 = browser.find_element_by_class_name('trollface.btn.btn-primary')
    button1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


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