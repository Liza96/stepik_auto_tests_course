from selenium import webdriver
import time

try:
    #link = "http://suninjuly.github.io/registration1.html" #первоначальный сайт
    link = "http://suninjuly.github.io/registration2.html" #сайт после изменений
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
    first_name.send_keys("Lizaveta")
    email = browser.find_element_by_css_selector(".first_block .form-control.third")
    email.send_keys("eliza@clever.ru")
    last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
    last_name.send_keys("Ivanova")

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()