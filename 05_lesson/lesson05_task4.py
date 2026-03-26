from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# открыть фаерфокс
driver = webdriver.Firefox()
print("открыли браузер")
sleep(2)

# перейти на нужную страницу
driver.get("http://the-internet.herokuapp.com/login")
print("перешли на страницу")
sleep(2)

# найти поле username и ввести tomsmith
# используем id="username"
driver.find_element(By.ID, "username").send_keys("tomsmith")
print("ввели username")
sleep(2)


# найти поле password и ввести SuperSecretPassword!
# используем id="password"
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
print("ввели password")
sleep(2)

# нажать кнопку Login
# ищем по тегу button с типом submit
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
print("нажали login")
sleep(2)


# найти заголовок h4 и вывести текст в консоль
# ищем по тегу h4 и классу subheader как на скриншоте
message = driver.find_element(By.CSS_SELECTOR, "h4.subheader").text
print(message)
print("вывели текст")
sleep(2)


# закрыть браузер
driver.quit()
