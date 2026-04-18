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
def test_fill_form():
    # Для Safari не нужно указывать сервис или путь к драйверу
    # просто запускаем браузер
    driver = webdriver.Safari()
    # Окно на весь экран
    driver.maximize_window()

    # 1. Открываем страницу
    # урл - переменная, чтобы поместилось в строку
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    # Ожидание (до 10 секунд)
    wait = WebDriverWait(driver, 10)

    # Ждем, пока поле "first-name" станет доступным
    # (подтверждаем загрузку страницы)
    wait.until(EC.element_to_be_clickable((By.NAME, "first-name")))

    # 2. Заполняем форму в виде словаря {имя_поля: значение}
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # В цикле находим каждое поле по имени и вводим туда текст
    for name, value in fields.items():
        driver.find_element(By.NAME, name).send_keys(value)
        # time.sleep(0.5)  # пауза (закомментить перед сдачей!)

    # Zip code оставляем пустым по условию, очищаем его на всякий случай
    driver.find_element(By.NAME, "zip-code").clear()

    # 3. Нажимаем кнопку Submit через CSS-селектор и кликаем
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Снова ждем (после клика), пока поле Zip code подгрузится в результатах
    # Проверяем по любому полю, что класс изменился
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    # time.sleep(1.5)  # пауза (закомментить перед сдачей!)

    # 4. Проверка: Zip code подсвечен красным (класс alert-danger)
    zip_code = driver.find_element(By.ID, "zip-code")
    zip_code_class = zip_code.get_attribute("class")
    assert "alert-danger" in zip_code_class

    # 5. Проверка: Остальные поля подсвечены зеленым (класс alert-success)
    other_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in other_fields:
        # Находим каждое поле по ID
        field_element = driver.find_element(By.ID, field_id)
        # Получаем его CSS-класс
        field_class = field_element.get_attribute("class")
        # Проверяем наличие "зеленого" класса
        assert "alert-success" in field_class, \
            f"Поле {field_id} не подсвечено зеленым"

    # time.sleep(1.5)  # пауза (закомментить перед сдачей!)
    driver.quit()
