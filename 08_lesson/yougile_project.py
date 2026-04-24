# этот файл нужен для того, чтобы собрать в одном месте всю работу с API

# чтобы брать данные из переменных окружения
import os
# здесь используем его, чтобы создавать уникальные названия проектов
import time
# библиотека, через которую отправляются HTTP-запросы
import requests


# базовый адрес API YouGile (по умолчанию задан yougile.com)
# если нужно, можно подставить свой адрес через переменную окружения
BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com")

# токен берем из переменной окружения
# чтобы не хранить секретные данные в коде
TOKEN = os.getenv("YOUGILE_TOKEN")


# эта функция проверяет, что токен вообще указан
def check_token():
    assert TOKEN, (
        "Токен не передан. "
        "Укажи его в переменной окружения YOUGILE_TOKEN."
    )


# эта функция проверяет, что токен правильный
def check_auth_response(response):
    assert response.status_code != 401, (
        "Токен неверный или просрочен. "
        "Сервер вернул ошибку 401."
    )
    assert response.status_code != 403, (
        "Доступ запрещен. "
        "Проверь токен. Сервер вернул ошибку 403."
    )


# эта функция собирает заголовки для запросов
# тот же headers из postman
def get_headers():
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }


# эта функция делает уникальное имя проекта:
# благодаря этому тесты можно запускать много раз подряд
# как работает:
# time.time() дает текущее время
# * 1000 переводит его в миллисекунды
# int(...) убирает дробную часть
# str(...) превращает число в строку
# потом к нему добавляется "API project "
# например, получается: API project 1713980001234
def make_project_title():
    return "API project " + str(int(time.time() * 1000))


# эта функция превращает ответ в json,
# чтобы можно было обращаться к элементам из словаря
# если в ответе нет json, она вернет пустой словарь
# эта штука тоже есть в postman, внизу
def get_response_json(response):
    try:
        return response.json()
    except ValueError:
        return {}


# эта функция создает проект
# отправляет POST-запрос на /api-v2/projects
def create_project(body):
    return requests.post(
        f"{BASE_URL}/api-v2/projects",
        json=body,
        headers=get_headers(),
        timeout=10,
    )


# эта функция изменяет проект по id
# что меняется:
# используется PUT
# в адрес подставляется project_id
def update_project(project_id, body):
    return requests.put(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        json=body,
        headers=get_headers(),
        timeout=10,
    )


# эта функция получает проект по id
# что она делает:
# отправляет GET-запрос
# получает данные одного проекта
def get_project(project_id):
    return requests.get(
        f"{BASE_URL}/api-v2/projects/{project_id}",
        headers=get_headers(),
        timeout=10,
    )
