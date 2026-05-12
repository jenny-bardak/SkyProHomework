# by нужен, чтобы указать способ поиска элемента на странице
from selenium.webdriver.common.by import By

# webdriver используется в аннотации типа параметра driver
# так в коде видно, что в метод передают объект браузера selenium
from selenium.webdriver.remote.webdriver import WebDriver

# webdriverwait ждёт выполнение условия до заданного таймаута
from selenium.webdriver.support.ui import WebDriverWait

# ec содержит готовые условия ожидания для selenium
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    """page object для страницы медленного калькулятора"""

    def __init__(self, driver: WebDriver) -> None:
        """
        создает объект страницы калькулятора

        :param driver: WebDriver, открытый браузер selenium
        :return: None, метод ничего не возвращает
        """
        # сохраняем объект браузера в экземпляр класса
        self.driver = driver

        # сохраняем url страницы калькулятора
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        # локатор поля, в котором задается задержка вычисления
        self._delay_input = (By.ID, "delay")

        # локатор экрана калькулятора, где появляется результат
        self._result_field = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """
        открывает страницу калькулятора

        :return: None, метод ничего не возвращает
        """
        # открываем страницу по сохраненному url
        self.driver.get(self.url)

    def set_delay(self, seconds: str) -> None:
        """
        вводит задержку вычисления

        :param seconds: str, количество секунд
        :return: None, метод ничего не возвращает
        """
        # находим поле задержки на странице
        delay = self.driver.find_element(*self._delay_input)

        # очищаем текущее значение поля
        delay.clear()

        # вводим новое значение задержки
        delay.send_keys(seconds)

    def click_button(self, text: str) -> None:
        """
        нажимает кнопку калькулятора по тексту

        :param text: str, текст кнопки
        :return: None, метод ничего не возвращает
        """
        # находим кнопку по тексту и нажимаем на нее
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def get_result(self, timeout: int, expected_text: str) -> str:
        """
        ждет нужный результат и возвращает текст с экрана калькулятора

        :param timeout: int, максимальное время ожидания в секундах
        :param expected_text: str, ожидаемый текст результата
        :return: str, текст с экрана калькулятора
        """
        # ждем, пока на экране калькулятора появится ожидаемый текст
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self._result_field,
                expected_text,
            )
        )

        # возвращаем фактический текст с экрана калькулятора
        return self.driver.find_element(*self._result_field).text


class LoginPage:
    """page object для страницы авторизации магазина"""

    def __init__(self, driver: WebDriver) -> None:
        """
        создает объект страницы авторизации

        :param driver: WebDriver, открытый браузер selenium
        :return: None, метод ничего не возвращает
        """
        # сохраняем объект браузера в экземпляр класса
        self.driver = driver

        # сохраняем url страницы авторизации
        self.url = "https://www.saucedemo.com/"

        # локатор поля логина
        self._user = (By.ID, "user-name")

        # локатор поля пароля
        self._password = (By.ID, "password")

        # локатор кнопки login
        self._login_button = (By.ID, "login-button")

    def open(self) -> None:
        """
        открывает страницу авторизации

        :return: None, метод ничего не возвращает
        """
        # открываем страницу по сохраненному url
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        вводит логин, пароль и нажимает кнопку login

        :param username: str, логин пользователя
        :param password: str, пароль пользователя
        :return: None, метод ничего не возвращает
        """
        # вводим логин в поле username
        self.driver.find_element(*self._user).send_keys(username)

        # вводим пароль в поле password
        self.driver.find_element(*self._password).send_keys(password)

        # нажимаем кнопку login
        self.driver.find_element(*self._login_button).click()


class ShopPage:
    """page object для страницы каталога товаров"""

    def __init__(self, driver: WebDriver) -> None:
        """
        создает объект страницы каталога

        :param driver: WebDriver, открытый браузер selenium
        :return: None, метод ничего не возвращает
        """
        # сохраняем объект браузера в экземпляр класса
        self.driver = driver

        # локатор кнопки добавления рюкзака
        self._backpack = (By.ID, "add-to-cart-sauce-labs-backpack")

        # локатор кнопки добавления футболки
        self._bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")

        # локатор кнопки добавления комбинезона
        self._onesie = (By.ID, "add-to-cart-sauce-labs-onesie")

        # локатор ссылки на корзину
        self._cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_items(self) -> None:
        """
        добавляет в корзину товары из задания

        :return: None, метод ничего не возвращает
        """
        # добавляем рюкзак в корзину
        self.driver.find_element(*self._backpack).click()

        # добавляем футболку в корзину
        self.driver.find_element(*self._bolt_tshirt).click()

        # добавляем комбинезон в корзину
        self.driver.find_element(*self._onesie).click()

    def go_to_cart(self) -> None:
        """
        переходит в корзину

        :return: None, метод ничего не возвращает
        """
        # нажимаем на ссылку корзины
        self.driver.find_element(*self._cart_button).click()


class CartPage:
    """page object для страницы корзины"""

    def __init__(self, driver: WebDriver) -> None:
        """
        создает объект страницы корзины

        :param driver: WebDriver, открытый браузер selenium
        :return: None, метод ничего не возвращает
        """
        # сохраняем объект браузера в экземпляр класса
        self.driver = driver

        # локатор кнопки checkout
        self._checkout_button = (By.ID, "checkout")

    def checkout(self) -> None:
        """
        нажимает кнопку checkout

        :return: None, метод ничего не возвращает
        """
        # нажимаем кнопку checkout
        self.driver.find_element(*self._checkout_button).click()


class CheckoutPage:
    """page object для страницы оформления заказа"""

    def __init__(self, driver: WebDriver) -> None:
        """
        создает объект страницы оформления заказа

        :param driver: WebDriver, открытый браузер selenium
        :return: None, метод ничего не возвращает
        """
        # сохраняем объект браузера в экземпляр класса
        self.driver = driver

        # локатор поля имени
        self._first_name = (By.ID, "first-name")

        # локатор поля фамилии
        self._last_name = (By.ID, "last-name")

        # локатор поля почтового индекса
        self._zip_code = (By.ID, "postal-code")

        # локатор кнопки continue
        self._continue_button = (By.ID, "continue")

        # локатор строки с итоговой суммой
        self._total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, name: str, surname: str, code: str) -> None:
        """
        заполняет форму оформления заказа

        :param name: str, имя покупателя
        :param surname: str, фамилия покупателя
        :param code: str, почтовый индекс
        :return: None, метод ничего не возвращает
        """
        # вводим имя покупателя
        self.driver.find_element(*self._first_name).send_keys(name)

        # вводим фамилию покупателя
        self.driver.find_element(*self._last_name).send_keys(surname)

        # вводим почтовый индекс
        self.driver.find_element(*self._zip_code).send_keys(code)

        # нажимаем кнопку continue
        self.driver.find_element(*self._continue_button).click()

    def get_total(self) -> str:
        """
        возвращает итоговую сумму заказа

        :return: str, итоговая сумма заказа
        """
        # получаем текст строки с итоговой суммой
        total_text = self.driver.find_element(*self._total_label).text

        # удаляем текст "total: " и возвращаем только сумму
        return total_text.replace("Total: ", "")
