# SkyProHomework

## Домашнее задание 10

В папке `10_lesson` лежат Selenium-тесты, переписанные с Page Object
из домашнего задания 7 и размеченные для Allure-отчета.

### Подготовка окружения

Установить Python-зависимости:

```bash
python3 -m pip install -r requirements.txt
```

Для просмотра отчета нужен Allure Commandline. На macOS его удобно
поставить через Homebrew:

```bash
brew install allure
```

### Запуск тестов с формированием Allure-результатов

Команда ниже запускает тесты и складывает служебные файлы отчета
в папку `10_lesson/allure-results`:

```bash
python3 -m pytest 10_lesson --alluredir=10_lesson/allure-results
```

### Просмотр сформированного отчета

Самый быстрый способ открыть отчет:

```bash
allure serve 10_lesson/allure-results
```

Если нужно сначала сгенерировать HTML-отчет в отдельную папку:

```bash
allure generate 10_lesson/allure-results -o 10_lesson/allure-report --clean
allure open 10_lesson/allure-report
```

Папки `10_lesson/allure-results` и `10_lesson/allure-report`
не нужно добавлять в pull request: они создаются локально при запуске.
