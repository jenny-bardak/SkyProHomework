"""Page Object страницы авторизации YouGile."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config import WEB_URL
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Действия пользователя на странице входа."""

    def __init__(self, driver: WebDriver) -> None:
        """Создает объект страницы входа.

        :param driver: открытый браузер Selenium
        :return: None
        """
        super().__init__(driver)

        # Фактическая страница входа в облачную версию YouGile.
        # Путь /team/ используется для открытия формы с email и паролем.
        self.url = f"{WEB_URL}/team/"

        self._email_locators = [
            (By.CSS_SELECTOR, "input[type='email']"),
            (By.CSS_SELECTOR, "input[name='email']"),
            (By.CSS_SELECTOR, "input[placeholder*='Email']"),
            (By.CSS_SELECTOR, "input[placeholder*='почт']"),
        ]
        self._password_locators = [
            (By.CSS_SELECTOR, "input[type='password']"),
            (By.CSS_SELECTOR, "input[name='password']"),
        ]
        self._submit = (
            By.XPATH,
            "//*[self::button or @role='button']"
            "[contains(normalize-space(), 'Войти') "
            "or contains(normalize-space(), 'Log In') "
            "or contains(normalize-space(), 'Login')]",
        )

    def open(self) -> None:
        """Открывает страницу входа.

        :return: None
        """
        self.driver.get(self.url)

    def login(self, email: str, password: str) -> None:
        """Вводит email, пароль и нажимает кнопку входа.

        :param email: email пользователя YouGile
        :param password: пароль пользователя YouGile
        :return: None
        """
        self.type_into_first_visible(self._email_locators, email)
        self.type_into_first_visible(self._password_locators, password)
        self.wait_clickable(self._submit).click()

    def assert_form_is_visible(self) -> None:
        """Проверяет, что форма входа отображается.

        :return: None
        """
        self.type_into_first_visible(self._email_locators, "")
        self.type_into_first_visible(self._password_locators, "")
        self.wait_clickable(self._submit)
