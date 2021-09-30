"""Задание: работа с выпадающим списком
Для этой задачи мы придумали еще один вариант капчи для роботов. Придется немного переобучить нашего робота, чтобы он справился с новым заданием.

Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.



Когда ваш код заработает, попробуйте запустить его на странице http://suninjuly.github.io/selects2.html. Ваш код и для нее тоже ﻿должен пройти успешно."""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
browser = webdriver.Chrome()

#link = 'http://suninjuly.github.io/selects1.html'
link ='http://suninjuly.github.io/selects2.html'

try:
    browser.get(link)
    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')
    num = int(num1.text) + int(num2.text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(num))  # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
    
