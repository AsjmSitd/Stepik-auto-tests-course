"""Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи."""
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/get_attribute.html"

try:
    browser.get(link)
    image = browser.find_element_by_id("treasure")
    x_element = image.get_attribute("valuex")
    x = x_element
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()

    
