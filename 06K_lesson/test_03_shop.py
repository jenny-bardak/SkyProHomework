# import time  # Импортируем для временных пауз (закомментить перед сдачей!)
# Основной модуль: отвечает за запуск и управление браузером
from selenium import webdriver
# Поисковик: предоставляет методы для поиска элементов (ID, Name, CSS и т.д.)
from selenium.webdriver.common.by import By


def test_shop_purchase():
    # 1. Открываем магазин в Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 2. Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.ID, "login-button").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 3. Добавление товаров в корзину
    # Ищем кнопки добавления по ID конкретных товаров
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 4. Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 5. Нажимаем Checkout
    driver.find_element(By.ID, "checkout").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 6. Заполнение формы данными
    driver.find_element(By.ID, "first-name").send_keys("Jenny")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.ID, "last-name").send_keys("Bardak")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 7. Нажимаем Continue
    driver.find_element(By.ID, "continue").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 8. Читаем итоговую стоимость
    # Ищем элемент, где написано "Total: $58.29"
    total_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    # 9. Проверка итоговой суммы
    # Мы проверяем, что в строке total_text содержится нужная сумма
    assert total_text == "Total: $58.29"

    # 10. Закрываем браузер
    driver.quit()
