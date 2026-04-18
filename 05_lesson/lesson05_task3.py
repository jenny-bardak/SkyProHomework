from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# открыть фаерфокс
driver = webdriver.Firefox()


# перейти на нужную страницу
driver.get("http://the-internet.herokuapp.com/inputs")


# найти поле ввода
# на этой странице поле ввода имеет тег input
input_field = driver.find_element(By.TAG_NAME, "input")


# ввести в поле текст 12345
input_field.send_keys("12345")
print("ввели 12345")
sleep(2)


# очистить это поле
input_field.clear()
print("очистили поле")
sleep(2)


# ввести в поле текст 54321
input_field.send_keys("54321")
print("ввели 54321")
sleep(2)


# закрыть браузер
driver.quit()
