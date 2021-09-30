"""Задание:

Какую ошибку вы увидите в консоли, если попытаетесь выполнить команду browser.find_element_by_id("button")
после открытия страницы http://suninjuly.github.io/cats.html?"""

from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button")
button.click()
#message = browser.find_element_by_id("verify_message")
#
#assert "successful" in message.text
