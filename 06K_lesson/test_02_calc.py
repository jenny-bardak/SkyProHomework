# import time  # Импортируем для временных пауз (закомментить перед сдачей!)
# Основной модуль: отвечает за запуск и управление браузером
from selenium import webdriver
# Поисковик: предоставляет методы для поиска элементов (ID, Name, CSS и т.д.)
from selenium.webdriver.common.by import By
# Инструмент ожидания: позволяет программе ждать определенное время,
# пока условие не выполнится
from selenium.webdriver.support.ui import WebDriverWait
# Набор условий: содержит готовые сценарии для ожидания
# (например, "элемент появился" или "текст изменился")
# называем его сокращенно "EC", чтобы код был короче и чище
from selenium.webdriver.support import expected_conditions as EC


# Функция ОБЯЗАТЕЛЬНО должна начинаться с test_
def test_slow_calculator():
    # Настройка драйвера (в данном примере Chrome)
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1. Открываем страницу
    # урл - переменная, чтобы поместилось в строку
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 2. Работаем с полем ввода задержки
    delay_input = driver.find_element(By.ID, "delay")
    # очищаем поле
    delay_input.clear()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    # Вводим значение 45
    delay_input.send_keys("45")
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 3. Нажимаем кнопки 7, +, 8, =
    # Мы ищем кнопки через XPath по тексту внутри них
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)
    driver.find_element(By.XPATH, "//span[text()='=']").click()
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # 4. Проверка результата
    # Нам нужно ждать 45 секунд
    # Это "умное" ожидание: оно проверяет экран калькулятора
    wait = WebDriverWait(driver, 45)

    # Ждем конкретное условие: 
    # когда в элементе с классом "screen" появится текст "15"
    wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )

    # Когда ожидание завершилось (текст появился),
    # берем этот текст для проверки
    result = driver.find_element(By.CLASS_NAME, "screen").text

    # Финальная проверка, что на экране именно 15
    assert result == "15"
    # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # Закрываем браузер
    driver.quit()
