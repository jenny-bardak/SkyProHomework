# Дипломный проект YouGile

Проект автоматизации UI- и API-проверок YouGile.

## Стек

- Python
- pytest
- Requests
- Selenium
- Allure

## Установка

```bash
cd ДИПЛОМ
python3 -m pip install -r requirements.txt
```

## Настройка переменных окружения

Создай локальный файл `.env` по примеру `.env.example` или экспортируй переменные в терминале.

Пример:

```bash
export YOUGILE_API_URL="https://ru.yougile.com/api-v2"
export YOUGILE_WEB_URL="https://ru.yougile.com"
export YOUGILE_TOKEN="твой_api_токен"
export YOUGILE_EMAIL="твой_email"
export YOUGILE_PASSWORD="твой_пароль"
```

## Запуск тестов

Все тесты:

```bash
python3 -m pytest --alluredir=allure-results
```

Только API-тесты:

```bash
python3 -m pytest -m "api" --alluredir=allure-results
```

Только UI-тесты:

```bash
python3 -m pytest -m "ui" --alluredir=allure-results
```

## Просмотр Allure-отчета

```bash
allure serve allure-results
```

Или генерация HTML-отчета:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```
