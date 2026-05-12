"""UI-автотесты дипломного проекта по YouGile."""

from uuid import uuid4

import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from config import EMAIL, PASSWORD
from pages.login_page import LoginPage
from pages.projects_page import ProjectsPage


def make_ui_title(prefix: str) -> str:
    """Создает уникальное название для UI-объекта.

    :param prefix: понятный префикс названия
    :return: уникальное название
    """
    return f"{prefix}_{uuid4().hex[:6]}"


def login_to_yougile(driver: WebDriver) -> ProjectsPage:
    """Авторизуется в YouGile и возвращает страницу проектов.

    :param driver: открытый браузер Selenium
    :return: объект ProjectsPage
    """
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу авторизации YouGile"):
        login_page.open()

    with allure.step("Ввести email, пароль и нажать кнопку входа"):
        login_page.login(EMAIL or "", PASSWORD or "")

    projects_page = ProjectsPage(driver)

    with allure.step("Дождаться открытия рабочего пространства"):
        projects_page.wait_workspace_opened()

    return projects_page


@pytest.mark.ui
@allure.title("Отображение формы авторизации YouGile")
@allure.story("UI. Авторизация")
def test_login_form_is_visible(driver: WebDriver) -> None:
    """Проверяет, что форма входа доступна пользователю."""
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу авторизации YouGile"):
        login_page.open()

    with allure.step("Проверить поля email, пароля и кнопку входа"):
        login_page.assert_form_is_visible()


@pytest.mark.ui
@allure.title("Успешная авторизация в YouGile")
@allure.story("UI. Авторизация")
def test_successful_login(driver: WebDriver) -> None:
    """Проверяет, что пользователь может войти в веб-интерфейс."""
    projects_page = login_to_yougile(driver)

    with allure.step("Проверить, что открылась рабочая область"):
        assert "login" not in driver.current_url.lower()
        projects_page.assert_text_visible("Проекты")


@pytest.mark.ui
@allure.title("Отображение списка проектов компании")
@allure.story("UI. Проекты")
def test_projects_list_is_visible(driver: WebDriver) -> None:
    """Проверяет, что пользователь видит список проектов компании."""
    projects_page = login_to_yougile(driver)

    with allure.step("Проверить заголовок и проекты в списке"):
        projects_page.assert_text_visible("Проекты компании")
        projects_page.assert_text_visible("Bardak Test")
        projects_page.assert_text_visible("Пример проекта")


@pytest.mark.ui
@allure.title("Открытие окна создания проекта")
@allure.story("UI. Проекты")
def test_open_create_project_modal(driver: WebDriver) -> None:
    """Проверяет открытие формы создания проекта."""
    projects_page = login_to_yougile(driver)

    with allure.step("Открыть окно создания проекта с задачами"):
        projects_page.open_create_project_modal()

    with allure.step("Проверить основные поля формы"):
        projects_page.assert_text_visible("Новый проект с задачами")
        projects_page.assert_text_visible("Название проекта")
        projects_page.assert_text_visible("Участники проекта")


@pytest.mark.ui
@allure.title("Создание проекта в веб-интерфейсе")
@allure.story("UI. Проекты")
def test_create_project(driver: WebDriver) -> None:
    """Проверяет создание проекта через UI."""
    projects_page = login_to_yougile(driver)
    project_title = make_ui_title("Diploma_UI_project")

    with allure.step("Создать новый проект с задачами"):
        projects_page.create_project(project_title)

    with allure.step("Проверить, что проект появился в списке"):
        projects_page.assert_text_visible(project_title)
