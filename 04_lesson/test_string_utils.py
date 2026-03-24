import pytest
from string_utils import StringUtils

# assert - "утверждаю, что...". Главная команда теста:
#          Если после assert получается True — тест пройден
#          Если False — тест упал с ошибкой.

# Создаем объект класса один раз, чтобы использовать его во всех тестах
utils = StringUtils()


# --- Тесты для метода capitalize (делает первую букву заглавной) ---
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),       # Позитивный: обычное слово
    ("hello world", "Hello world"),  # Позитивный: строка с пробелом
    ("123", "123"),             # Позитивный: цифры (не меняются)
    ("", ""),                   # Негативный: пустая строка
    (" ", " "),                 # Негативный: строка из пробела
    ("Skypro", "Skypro")        # Позитивный: уже с заглавной
])
def test_capitalize(input_str, expected):
    # Вызываем метод и проверяем, что результат совпал с ожидаемым (expected)
    assert utils.capitalize(input_str) == expected


# --- Тесты для метода trim (удаляет пробелы в начале) ---
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),    # Позитивный: пробелы в начале
    ("skypro   ", "skypro   "),  # Позитивный: пробелы в конце (не удаляются)
    ("   ", ""),                # Позитивный: только пробелы
    ("skypro", "skypro"),       # Позитивный: пробелов нет
    ("  hello world", "hello world")  # Позитивный: пробелы перед фразой
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


# --- Тесты для метода contains (проверка наличия символа/подстроки) ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),      # Позитивный: символ есть (регистр совпадает)
    ("SkyPro", "U", False),     # Позитивный: символа нет
    ("SkyPro", "Pro", True),    # Позитивный: поиск целой подстроки
    ("", "a", False),           # Негативный: поиск в пустой строке
    ("123", "1", True),         # Позитивный: поиск цифры
    ("SkyPro", "s", False)      # Негативный: другой регистр (маленькая 's')
])
def test_contains(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


# --- Тесты для метода delete_symbol (удаление части строки) ---
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),   # Позитивный: удаление одной буквы
    ("SkyPro", "Pro", "Sky"),   # Позитивный: удаление подстроки
    ("banana", "a", "bnn"),     # Позитивный: удаление повторяющихся букв 'a'
    ("SkyPro", "z", "SkyPro"),  # Позитивный: удаление несуществующего символа
    ("", "a", ""),              # Негативный: удаление из пустой строки
    ("SkyPro", "", "SkyPro")    # Негативный: передача пустой стр для удаления
])
def test_delete_symbol(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
