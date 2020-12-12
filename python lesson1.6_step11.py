"""Попробуйте запустить код из предыдущего шага, указав в качестве начальной страницы новую ссылку. Если ваш тест упал с ошибкой NoSuchElementException, это означает, что вы выбрали правильные селекторы и смогли обнаружить баг, который создали разработчики. Это хорошо! Значит, ваши тесты сработали как надо. Пугаться не стоит, здесь ошибка в приложении которое вы тестируете, а не в вашем тесте.

Если же ваш тест прошел успешно, то это означает, что тест пропустил серьезный баг. В этом случае попробуйте поменять селекторы, сделав их уникальными. После изменения убедитесь, что ваш тест исправно проходит в старой версии страницы.

Чтобы получить максимальное количество баллов, прежде чем отправлять решение на рецензию, самостоятельно убедитесь в том что:

Тест успешно проходит на странице http://suninjuly.github.io/registration1.html﻿

Тест падает с ошибкой NoSuchElementException http://suninjuly.github.io/registration2.html

Используемые селекторы должны быть уникальны

Будьте внимательны, ведь на рецензирование работу можно отправить только один раз! """
from selenium import webdriver
import time

try:
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(".first_block .form-group.first_class input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .form-group.second_class input")
    input2.send_keys("White")
    input3 = browser.find_element_by_css_selector(".first_block .form-group.third_class input")
    input3.send_keys("It's email, believe me!")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций".first_block input[placeholder='Input your first name']"
    browser.quit()