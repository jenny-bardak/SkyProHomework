from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (в данном примере Chrome)
driver = webdriver.Chrome()

try:
    # 1. Переходим на страницу
    driver.get("http://uitestingplayground.com/ajax")

    # 2. Находим синюю кнопку и нажимаем на нее
    blue_button = driver.find_element(By.ID, "ajaxButton")
    blue_button.click()

    # 3. Ждем появления зеленой плашки (используем явное ожидание вместо sleep)
    # Текст появляется не сразу, поэтому ждем его присутствия в DOM
    wait = WebDriverWait(driver, 20)
    green_banner = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    # 4. Получаем текст и выводим в консоль
    print(green_banner.text)

finally:
    # Закрываем браузер
    driver.quit()
