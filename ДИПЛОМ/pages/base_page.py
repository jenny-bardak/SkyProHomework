"""Базовые методы для страниц YouGile.

Эти методы помогают не повторять одинаковый Selenium-код в каждом Page Object.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import UI_TIMEOUT


class BasePage:
    """Общие действия, которые нужны разным страницам."""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет браузер и объект ожидания.

        :param driver: открытый браузер Selenium
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, UI_TIMEOUT)

    def wait_visible(self, locator: tuple[str, str]) -> WebElement:
        """Ждет, пока элемент появится и станет видимым.

        :param locator: Selenium-локатор, например (By.CSS_SELECTOR, "button")
        :return: найденный WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator: tuple[str, str]) -> WebElement:
        """Ждет, пока по элементу можно будет кликнуть.

        :param locator: Selenium-локатор
        :return: найденный WebElement
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_text(self, text: str) -> None:
        """Кликает по кнопке или ссылке с указанным текстом.

        :param text: видимый текст элемента
        :return: None
        """
        locator = (
            By.XPATH,
            "//*[self::button or self::a or @role='button']"
            f"[contains(normalize-space(), '{text}')]",
        )
        self.wait_clickable(locator).click()

    def click_last_visible_text(self, text: str) -> None:
        """Кликает по последнему видимому элементу с указанным текстом.

        Метод нужен для модальных окон YouGile: текст кнопки может
        повторяться в меню и в самой форме, а нажать нужно именно нижнюю
        кнопку подтверждения.

        :param text: видимый текст элемента
        :return: None
        """
        locator = (
            By.XPATH,
            f"//*[normalize-space()='{text}']",
        )

        def find_last_visible(driver: WebDriver) -> object:
            elements = driver.find_elements(*locator)
            visible_elements = [
                item for item in elements if item.is_displayed()
            ]
            if visible_elements:
                return visible_elements[-1]

            return False

        self.wait.until(find_last_visible).click()

    def page_contains(self, text: str) -> bool:
        """Проверяет, что текст появился на странице.

        :param text: ожидаемый текст
        :return: True, если текст есть в body страницы
        """
        locator = (By.XPATH, f"//*[contains(normalize-space(), '{text}')]")
        elements = self.driver.find_elements(*locator)
        return len(elements) > 0

    def wait_text_visible(self, text: str) -> None:
        """Ждет появления текста на странице.

        :param text: ожидаемый текст
        :return: None
        """
        locator = (By.XPATH, f"//*[contains(normalize-space(), '{text}')]")
        self.wait.until(EC.visibility_of_element_located(locator))

    def type_into_first_visible(
        self,
        locators: list[tuple[str, str]],
        value: str,
    ) -> None:
        """Вводит текст в первое найденное видимое поле.

        Такой метод полезен для учебного проекта: если верстка слегка меняется,
        тест всё равно часто находит поле по одному из запасных локаторов.

        :param locators: список возможных локаторов поля
        :param value: текст для ввода
        :return: None
        """
        def find_visible_field(driver: WebDriver) -> object:
            """Ищет первое видимое поле по списку локаторов."""
            for locator in locators:
                elements = driver.find_elements(*locator)
                visible_elements = [
                    item for item in elements if item.is_displayed()
                ]
                if visible_elements:
                    return visible_elements[0]

            return False

        # Форма YouGile дорисовывается JavaScript-ом, поэтому здесь нужно
        # дождаться поля, а не искать его мгновенно после открытия URL.
        field = self.wait.until(find_visible_field)
        field.clear()
        field.send_keys(value)
