from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

# Разбиваем длинную ссылку внутри скобок
url = (
    "https://bonigarcia.dev"
    "/selenium-webdriver-java/"
    "loading-images.html"
)

try:
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    # Ждем, когда появится хотя бы 4 картинки в DOM
    # Метод называется: presence_of_all_elements_located
    wait.until(
        lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 4
    )

    # Теперь находим их все
    images = driver.find_elements(By.TAG_NAME, "img")

    # Берем 3-ю по счету (индекс 2)
    print(images[2].get_attribute("src"))


finally:
    driver.quit()
