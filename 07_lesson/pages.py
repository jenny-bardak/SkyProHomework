# Поисковик: предоставляет методы для поиска элементов (ID, Name, CSS и т.д.)
from selenium.webdriver.common.by import By
# Инструмент ожидания: позволяет программе ждать определенное время,
# пока условие не выполнится
from selenium.webdriver.support.ui import WebDriverWait
# Набор условий: содержит готовые сценарии для ожидания
# (например, "элемент появился" или "текст изменился")
# называем его сокращенно "EC", чтобы код был короче и чище
from selenium.webdriver.support import expected_conditions as EC


# Это КЛАСС страницы. В нем объединяем все данные о калькуляторе:
# его адрес, кнопки и действия, которые он умеет выполнять.
# -- Зачем это нужно? --
# 1) Порядок: Мы отделяем описание страницы (как она выглядит и где её кнопки)
# от логики теста (что именно мы проверяем)
# 2) Удобство: Если на сайте завтра поменяют ID кнопки,
# не придется перерывать 100 тестов:
# зайдешь в этот класс, поменяешь одну строчку, и все тесты снова заработают.
# 3) Переиспользование: Если понадобится второй тест
# для этого же калькулятора, не нужно заново искать кнопки:
# просто возьмешь этот уже готовый класс.
class CalcPage:
    # Инициализация: когда мы создаем объект страницы, он запоминает драйвер
    # Этот МЕТОД (то же, что и функция, но внутри класса)
    # — "входная дверь". Он срабатывает сам, когда мы в тесте
    # создаем страницу, и принимает внутрь открытое окно браузера (driver).
    def __init__(self, driver):
        # А эта строчка — "память" страницы. Мы заставляем её ЗАПОМНИТЬ
        # полученный браузер, чтобы она могла управлять им в других фун-ях ниже
        self.driver = driver
        # Ссылка на страницу. Разбита на две части,
        # чтобы Flake8 не ругался на длину
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        # Локаторы
        # -- Адресная книга элементов --
        # Мы заранее даем техническим адресам (ID, CSS) понятные имена
        # Если адрес на сайте изменится, поправим его только здесь.

        # Записываем путь к полю, в которое вводится время задержки
        self._delay_input = (By.ID, "delay")
        # Записываем путь к дисплею (экрану) калькулятора, где будет результат
        self._result_field = (By.CSS_SELECTOR, ".screen")

    # МЕТОД:
    # открывает браузер и переходит по ссылке, которую мы записали выше
    def open(self):
        self.driver.get(self.url)

    # МЕТОД: настраивает время задержки в калькуляторе.
    def set_delay(self, seconds):
        # Находим поле задержки, используя адрес из нашей "адресной книги".
        # Звездочка (*) помогает программе
        # правильно прочитать кортеж (By.ID, "delay")
        delay = self.driver.find_element(*self._delay_input)
        # Очищаем поле от цифры "0", которая стоит там по умолчанию
        delay.clear()
        # Печатаем наше время (например, "45")
        delay.send_keys(seconds)

    # МЕТОД: нажимает на любую кнопку калькулятора по её тексту
    def click_button(self, text):
        # Мы ищем на странице текст (7, 8, + или =), который передали из теста
        # Конструкция f"//span[text()='{text}']" — это точный поисковый запрос
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    # МЕТОД: умеет ждать и забирать финальный результат
    def get_result(self, timeout):
        # Включаем "умное ожидание": программа будет смотреть на дисплей
        # и ждать (максимум 50 сек), пока там не появится именно число "15"
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self._result_field, "15")
        )
        # Как только число появилось, забираем его и отправляем обратно в тест
        return self.driver.find_element(*self._result_field).text


# --- ДЛЯ ВТОРОГО ЗАДАНИЯ ---
# КЛАСС страницы авторизации
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        # Адреса полей и кнопки
        self._user = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._btn = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.url)

    # МЕТОД: вводит данные и жмет "Login"
    def login(self, username, password):
        self.driver.find_element(*self._user).send_keys(username)
        self.driver.find_element(*self._pass).send_keys(password)
        self.driver.find_element(*self._btn).click()


# КЛАСС главной страницы магазина (каталог)
class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        # Локаторы кнопок добавления конкретных товаров
        self._backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self._bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self._onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self._cart_btn = (By.CLASS_NAME, "shopping_cart_link")

    # МЕТОД: добавляет три нужных товара
    def add_items(self):
        self.driver.find_element(*self._backpack).click()
        self.driver.find_element(*self._bolt_tshirt).click()
        self.driver.find_element(*self._onesie).click()

    # МЕТОД: переходит в корзину
    def go_to_cart(self):
        self.driver.find_element(*self._cart_btn).click()


# КЛАСС страницы корзины
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self._checkout_btn = (By.ID, "checkout")

    # МЕТОД: нажимает кнопку оформления заказа
    def checkout(self):
        self.driver.find_element(*self._checkout_btn).click()


# КЛАСС оформления заказа (Checkout)
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self._first_name = (By.ID, "first-name")
        self._last_name = (By.ID, "last-name")
        self._zip = (By.ID, "postal-code")
        self._continue_btn = (By.ID, "continue")
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    # МЕТОД: заполняет форму данными пользователя
    def fill_form(self, name, surname, code):
        self.driver.find_element(*self._first_name).send_keys(name)
        self.driver.find_element(*self._last_name).send_keys(surname)
        self.driver.find_element(*self._zip).send_keys(code)
        self.driver.find_element(*self._continue_btn).click()

    # МЕТОД: забирает итоговую сумму со страницы
    def get_total(self):
        # Забираем текст "Total: $58.29"
        total_text = self.driver.find_element(*self._total_label).text
        # Оставляем только "$58.29" (убираем слово Total:)
        return total_text.replace("Total: ", "")
