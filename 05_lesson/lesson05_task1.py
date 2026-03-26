from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# открыть хром
driver = webdriver.Chrome()


# перейти на нужную страницу
driver.get("http://uitestingplayground.com/classattr")


# тыкнуть на синюю кнопку
# CSS-селектор для поиска кнопки с классом btn-primary
# искать элемент, у которого в атрибуте class есть 'btn-primary'
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
blue_button.click()


# появится модальное окно (alert)
# добавить паузу
sleep(3)


# закрыть алерт (переключает на алерт и тыкает ОК/принять)
driver.switch_to.alert.accept()


# закрыть браузер (надо для старых версий selenium, но считается хорошим тоном)
driver.quit()
