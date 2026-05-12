"""Page Object для базовых действий с проектами YouGile."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class ProjectsPage(BasePage):
    """Действия в рабочем пространстве YouGile."""

    def __init__(self, driver: WebDriver) -> None:
        """Создает объект страницы проектов.

        :param driver: открытый браузер Selenium
        :return: None
        """
        super().__init__(driver)

        self._body = (By.TAG_NAME, "body")
        self._text_input = [
            (By.CSS_SELECTOR, "input[placeholder*='название проекта']"),
            (By.CSS_SELECTOR, "input[type='text']"),
            (By.CSS_SELECTOR, "textarea"),
        ]

    def wait_workspace_opened(self) -> None:
        """Ждет открытия основного интерфейса после авторизации.

        :return: None
        """
        self.wait_visible(self._body)
        self.wait_text_visible("Проекты")

    def create_project(self, title: str) -> None:
        """Создает проект через интерфейс.

        :param title: название проекта
        :return: None
        """
        self.open_create_project_modal()
        self.type_into_first_visible(self._text_input, title)
        self.click_last_visible_text("Добавить проект с задачами")

    def open_create_project_modal(self) -> None:
        """Открывает окно создания проекта с задачами.

        :return: None
        """
        self.click_last_visible_text("Добавить проект с задачами")
        self.wait_text_visible("Новый проект с задачами")

    def assert_text_visible(self, text: str) -> None:
        """Проверяет, что нужный текст есть на странице.

        :param text: ожидаемый текст
        :return: None
        """
        self.wait_text_visible(text)
