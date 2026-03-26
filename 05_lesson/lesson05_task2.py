from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# открыть хром
driver = webdriver.Chrome()


# перейти на нужную страницу
driver.get("http://uitestingplayground.com/dynamicid")


# сохранить селектор в переменную
# ищем тег button с классом btn-primary
path = "button.btn-primary"


# тыкнуть на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, path)
blue_button.click()

# проверка клика
print("Клик выполнен успешно!")

# добавить паузу
sleep(3)


# закрыть браузер
driver.quit()
