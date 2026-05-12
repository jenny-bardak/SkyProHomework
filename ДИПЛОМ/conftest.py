"""Общие фикстуры pytest для дипломного проекта.

Фикстура — это подготовка данных или окружения для теста. Например,
здесь фикстура создает API-клиент или открывает браузер Selenium.
"""

from collections.abc import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

from api.yougile_api import YouGileApi
from config import API_URL, BROWSER, EMAIL, HEADLESS, PASSWORD, TOKEN


@pytest.fixture
def api_client() -> YouGileApi:
    """Создает API-клиент YouGile для каждого API-теста.

    :return: объект YouGileApi
    """
    if not TOKEN:
        pytest.skip("Для API-тестов нужна переменная окружения YOUGILE_TOKEN.")

    return YouGileApi(API_URL, TOKEN)


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Открывает браузер для UI-теста и закрывает его после проверки.

    :yield: объект Selenium WebDriver
    """
    if not EMAIL or not PASSWORD:
        pytest.skip(
            "Для UI-тестов нужны переменные YOUGILE_EMAIL и YOUGILE_PASSWORD."
        )

    if BROWSER == "firefox":
        options = FirefoxOptions()
        if HEADLESS:
            options.add_argument("-headless")
        browser = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        if HEADLESS:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        browser = webdriver.Chrome(options=options)

    browser.maximize_window()

    yield browser

    browser.quit()
