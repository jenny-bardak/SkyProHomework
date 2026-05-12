"""Настройки дипломного проекта.

Файл специально сделан простым: он читает данные из переменных окружения.
Так мы не храним токены, логины и пароли в коде и спокойно показываем
проект в публичном GitHub-репозитории.
"""

import os
from pathlib import Path
from typing import Optional


def load_env_file() -> None:
    """Подгружает переменные из локального .env без сторонних библиотек.

    Такой вариант удобен для учебного проекта: не добавляем лишнюю зависимость,
    но можем хранить настройки локально и не коммитить секреты в GitHub.

    :return: None
    """
    env_path = Path(__file__).parent / ".env"

    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped_line = line.strip()

        # Пустые строки и комментарии пропускаем.
        if not stripped_line or stripped_line.startswith("#"):
            continue

        # В .env ожидаем простой формат KEY=value.
        if "=" not in stripped_line:
            continue

        key, value = stripped_line.split("=", 1)

        # setdefault не перезаписывает переменную, если она уже задана
        # в терминале или CI. Это делает поведение предсказуемым.
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env_file()


# Базовый URL API. rstrip("/") убирает лишний слеш в конце,
# чтобы дальше URL собирались аккуратно: base_url + "/projects".
API_URL: str = os.getenv(
    "YOUGILE_API_URL",
    "https://ru.yougile.com/api-v2",
).rstrip("/")

# Базовый URL веб-интерфейса. Его можно заменить, если аккаунт работает
# на другом домене или в коробочной версии YouGile.
WEB_URL: str = os.getenv(
    "YOUGILE_WEB_URL",
    "https://ru.yougile.com",
).rstrip("/")

# Токен API. Если переменная пустая, API-фикстура аккуратно пропустит тесты.
TOKEN: Optional[str] = os.getenv("YOUGILE_TOKEN")

# Логин и пароль для UI-тестов. Их тоже передаем через окружение.
EMAIL: Optional[str] = os.getenv("YOUGILE_EMAIL")
PASSWORD: Optional[str] = os.getenv("YOUGILE_PASSWORD")

# Браузер можно переключить без правки кода.
BROWSER: str = os.getenv("BROWSER", "chrome").lower()

# Headless-режим удобен для CI, но для видеозащиты лучше открыть окно браузера.
HEADLESS: bool = os.getenv("HEADLESS", "false").lower() == "true"

# Таймаут ожиданий Selenium. Явные ожидания лучше, чем time.sleep(),
# потому что тест ждет ровно столько, сколько нужно странице.
UI_TIMEOUT: int = int(os.getenv("UI_TIMEOUT", "20"))
