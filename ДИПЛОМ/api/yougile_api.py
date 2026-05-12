"""Небольшой API-клиент для REST API YouGile.

Клиент нужен, чтобы тесты были читаемыми: в тестах мы описываем сценарий,
а детали HTTP-запросов лежат в одном месте.
"""

from typing import Any

import requests


class YouGileApi:
    """Класс-обертка над основными API-методами проектов YouGile."""

    def __init__(self, base_url: str, token: str, timeout: int = 15) -> None:
        """Создает сессию для запросов к API.

        :param base_url: базовый адрес API,
            например https://ru.yougile.com/api-v2
        :param token: API-токен YouGile
        :param timeout: максимальное ожидание ответа сервера в секундах
        :return: None
        """
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

        # Session хранит общие заголовки, поэтому их не надо повторять
        # в каждом отдельном запросе.
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        )

    def get_projects(self) -> requests.Response:
        """Получает список проектов.

        :return: объект Response с кодом, заголовками и телом ответа
        """
        return self.session.get(
            f"{self.base_url}/projects",
            timeout=self.timeout,
        )

    def create_project(self, title: str) -> requests.Response:
        """Создает проект с указанным названием.

        :param title: название нового проекта
        :return: объект Response от сервера
        """
        return self.session.post(
            f"{self.base_url}/projects",
            json={"title": title},
            timeout=self.timeout,
        )

    def create_project_raw(self, body: dict[str, Any]) -> requests.Response:
        """Отправляет произвольное тело в POST /projects.

        Метод нужен для негативных API-проверок, например для пустого body.

        :param body: JSON-тело запроса
        :return: объект Response от сервера
        """
        return self.session.post(
            f"{self.base_url}/projects",
            json=body,
            timeout=self.timeout,
        )

    def get_project(self, project_id: str) -> requests.Response:
        """Получает проект по id.

        :param project_id: идентификатор проекта
        :return: объект Response от сервера
        """
        return self.session.get(
            f"{self.base_url}/projects/{project_id}",
            timeout=self.timeout,
        )

    def update_project(
        self,
        project_id: str,
        title: str,
    ) -> requests.Response:
        """Обновляет название проекта.

        :param project_id: идентификатор проекта
        :param title: новое название проекта
        :return: объект Response от сервера
        """
        return self.session.put(
            f"{self.base_url}/projects/{project_id}",
            json={"title": title},
            timeout=self.timeout,
        )


def response_json(response: requests.Response) -> dict[str, Any]:
    """Безопасно превращает ответ API в словарь.

    Если сервер по какой-то причине вернул не JSON, тест получит пустой
    словарь и сможет показать понятную ошибку в assertion.

    :param response: ответ requests
    :return: тело ответа в виде dict или пустой dict
    """
    try:
        body = response.json()
    except ValueError:
        return {}

    if isinstance(body, dict):
        return body

    return {}
