# функция, принимающая 1 аргумент - год (число)
# возвращающая True, если год високосный
# и False - если нет
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# пример года
year = int(input("Введите год для проверки: "))


# вызывает функцию и передает год, а рез-т сохр в переменную result
result = is_leap_year(year)


# вывод в консоль ответ: <номер года>: <Tr|Fa>
print(f"Год {year} - високосный: {result}")
