# берем из основного файла готовые функции
from yougile_project import (
    check_auth_response,
    check_token,
    create_project,
    get_project,
    get_response_json,
    make_project_title,
    update_project,
)


# эта функция нужна только внутри тестов:
# создает проект, чтобы потом с ним работать в других проверках,
# поскольку в нескольких тестах нужен уже существующий проект
# что она делает:
# создает уникальное имя проекта
# отправляет запрос на создание
# получает ответ
# проверяет, что проект создался
# возвращает id, title проекта
def create_test_project():
    project_title = make_project_title()
    response = create_project({"title": project_title})
    check_auth_response(response)
    response_json = get_response_json(response)

    # проверяем, что проект создался
    assert response.status_code == 201
    assert "id" in response_json

    return response_json["id"], project_title


# ПОЗИТИВНЫЙ тест: проект можно создать
def test_create_project_positive():
    # проверяем, что токен указан
    check_token()

    # отправляем запрос на создание проекта
    project_title = make_project_title()
    response = create_project({"title": project_title})
    check_auth_response(response)
    response_json = get_response_json(response)

    # проверяем, что проект создался
    assert response.status_code == 201
    assert "id" in response_json

    # дополнительно проверяем, что проект существует (по id)
    project_id = response_json["id"]
    project_response = get_project(project_id)
    check_auth_response(project_response)
    project_json = get_response_json(project_response)

    assert project_response.status_code == 200
    assert project_json["id"] == project_id
    assert project_json["title"] == project_title


# НЕГАТИВНЫЙ тест: создать проект без названия
def test_create_project_negative_without_title():
    # проверяем, что токен указан
    check_token()

    # отправляем запрос без обязательного поля title
    response = create_project({})
    check_auth_response(response)

    # проверяем, что сервер вернул ошибку
    assert response.status_code == 400


# ПОЗИТИВНЫЙ тест: проект можно изменить
def test_update_project_positive():
    # проверяем, что токен указан
    check_token()

    # создаем проект
    project_id, old_title = create_test_project()

    # меняем название проекта
    new_title = old_title + " updated"
    response = update_project(project_id, {"title": new_title})
    check_auth_response(response)
    response_json = get_response_json(response)

    # проверяем, что изменение прошло успешно
    assert response.status_code == 200
    assert response_json["id"] == project_id

    # проверяем через GET, что название действительно изменилось
    project_response = get_project(project_id)
    check_auth_response(project_response)
    project_json = get_response_json(project_response)

    assert project_response.status_code == 200
    assert project_json["title"] == new_title


# НЕГАТИВНЫЙ тест: изменить проект с несуществующим id
def test_update_project_negative_wrong_id():
    # проверяем, что токен указан
    check_token()

    # берем id, которого не должно быть в системе
    wrong_project_id = "00000000-0000-0000-0000-000000000000"

    # пробуем изменить несуществующий проект
    response = update_project(wrong_project_id, {"title": "New title"})
    check_auth_response(response)

    # проверяем, что сервер вернул ошибку.
    assert response.status_code == 404


# ПОЗИТИВНЫЙ тест: проект можно получить по id
def test_get_project_positive():
    # проверяем, что токен указан
    check_token()

    # сначала создаем проект
    project_id, project_title = create_test_project()

    # получаем проект по id
    response = get_project(project_id)
    check_auth_response(response)
    response_json = get_response_json(response)

    # проверяем, что получили нужный проект
    assert response.status_code == 200
    assert response_json["id"] == project_id
    assert response_json["title"] == project_title
    assert "timestamp" in response_json


# НЕГАТИВНЫЙ тест: получить проект с несуществующим id
def test_get_project_negative_wrong_id():
    # проверяем, что токен указан
    check_token()

    # берем id, которого не должно быть в системе
    wrong_project_id = "00000000-0000-0000-0000-000000000000"

    # пробуем получить несуществующий проект
    response = get_project(wrong_project_id)
    check_auth_response(response)

    # проверяем, что сервер вернул ошибку
    assert response.status_code == 404
