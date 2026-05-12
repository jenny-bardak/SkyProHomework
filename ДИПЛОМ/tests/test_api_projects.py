"""API-автотесты дипломного проекта по YouGile."""

from uuid import uuid4

import allure
import pytest

from api.yougile_api import YouGileApi, response_json


def make_title(prefix: str) -> str:
    """Создает уникальное название, чтобы тесты не мешали друг другу.

    :param prefix: понятный префикс для названия объекта
    :return: уникальное название
    """
    return f"{prefix}_{uuid4().hex[:8]}"


def create_project_for_test(api_client: YouGileApi) -> tuple[str, str]:
    """Создает проект и возвращает его id и title.

    :param api_client: API-клиент YouGile
    :return: кортеж из id проекта и его названия
    """
    title = make_title("diploma_api_project")

    with allure.step("Создать тестовый проект через API"):
        response = api_client.create_project(title)
        body = response_json(response)

    assert response.status_code == 201, response.text
    assert "id" in body, f"В ответе нет id проекта: {body}"

    return body["id"], title


@pytest.mark.api
@allure.title("Получение списка проектов")
@allure.story("API. Проекты")
def test_get_projects_list(api_client: YouGileApi) -> None:
    """Проверяет, что список проектов доступен авторизованному пользователю."""
    with allure.step("Отправить GET /projects"):
        response = api_client.get_projects()

    with allure.step("Проверить успешный статус ответа"):
        assert response.status_code == 200, response.text


@pytest.mark.api
@allure.title("Создание проекта")
@allure.story("API. Проекты")
def test_create_project(api_client: YouGileApi) -> None:
    """Проверяет позитивное создание проекта."""
    title = make_title("diploma_api_create")

    with allure.step("Отправить POST /projects с названием проекта"):
        response = api_client.create_project(title)
        body = response_json(response)

    with allure.step("Проверить, что проект создан"):
        assert response.status_code == 201, response.text
        assert "id" in body, f"В ответе нет id проекта: {body}"


@pytest.mark.api
@allure.title("Получение проекта по id")
@allure.story("API. Проекты")
def test_get_project_by_id(api_client: YouGileApi) -> None:
    """Проверяет получение конкретного проекта по id."""
    project_id, title = create_project_for_test(api_client)

    with allure.step("Отправить GET /projects/{id}"):
        response = api_client.get_project(project_id)
        body = response_json(response)

    with allure.step("Проверить данные проекта в ответе"):
        assert response.status_code == 200, response.text
        assert body["id"] == project_id
        assert body["title"] == title


@pytest.mark.api
@allure.title("Изменение названия проекта")
@allure.story("API. Проекты")
def test_update_project_title(api_client: YouGileApi) -> None:
    """Проверяет изменение названия проекта через API."""
    project_id, _ = create_project_for_test(api_client)
    new_title = make_title("diploma_api_updated")

    with allure.step("Отправить PUT /projects/{id} с новым названием"):
        response = api_client.update_project(project_id, new_title)

    with allure.step("Проверить успешный статус обновления"):
        assert response.status_code == 200, response.text

    with allure.step("Получить проект и проверить новое название"):
        get_response = api_client.get_project(project_id)
        body = response_json(get_response)

    assert get_response.status_code == 200, get_response.text
    assert body["title"] == new_title


@pytest.mark.api
@allure.title("Создание проекта без обязательного названия")
@allure.story("API. Проекты")
def test_create_project_without_title(api_client: YouGileApi) -> None:
    """Проверяет негативный сценарий создания проекта без title."""
    with allure.step("Отправить POST /projects с пустым JSON"):
        response = api_client.create_project_raw({})

    with allure.step("Проверить, что сервер вернул ошибку валидации"):
        assert response.status_code == 400, response.text


@pytest.mark.api
@allure.title("Получение проекта с несуществующим id")
@allure.story("API. Проекты")
def test_get_project_with_wrong_id(api_client: YouGileApi) -> None:
    """Проверяет негативный сценарий получения проекта с неверным id."""
    wrong_project_id = "00000000-0000-0000-0000-000000000000"

    with allure.step("Отправить GET /projects/{id} с несуществующим id"):
        response = api_client.get_project(wrong_project_id)

    with allure.step("Проверить, что сервер вернул 404"):
        assert response.status_code == 404, response.text
