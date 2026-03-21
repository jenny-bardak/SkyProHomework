from smartphone import Smartphone

# Создаем пустой список
catalog = []

# Наполняем список пятью экземплярами класса
catalog.append(Smartphone("Apple", "iPhone 15", "+79001112233"))
catalog.append(Smartphone("Samsung", "Galaxy S23", "+79112223344"))
catalog.append(Smartphone("Xiaomi", "13T Pro", "+79223334455"))
catalog.append(Smartphone("Google", "Pixel 8", "+79334445566"))
catalog.append(Smartphone("Huawei", "P60 Pro", "+79445556677"))

# Цикл для печати каталога
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
