"""Задание: загрузка файла
В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"""
import os
#
#current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
#file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)


from selenium import webdriver
import time

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/file_input.html"

    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("White")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("It's email, believe me!")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, ' ')  # добавляем к этому пути имя файла
    file_button = browser.find_element_by_id('file')
    file_button.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()