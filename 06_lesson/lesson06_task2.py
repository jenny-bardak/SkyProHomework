from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    # Находим поле ввода и печатаем текст
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    # Находим кнопку и кликаем по ней
    button = driver.find_element(By.ID, "updatingButton")
    button.click()

    # Выводим новый текст кнопки
    print(button.text)

finally:
    driver.quit()
