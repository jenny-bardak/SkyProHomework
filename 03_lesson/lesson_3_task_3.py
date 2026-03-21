from address import Address
from mailing import Mailing

to_addr = Address("111000", "Москва", "Арбат", "11", "1")
from_addr = Address("100100", "Королёв", "Площадь Ленина", "1", "10")

my_mailing = Mailing(to_addr, from_addr, 500, "TRACK007")

# собираем части в одну переменную
# скобки позволяют переносить строки без использования лишних символов
message = (
    f"Отправление {my_mailing.track} из {my_mailing.from_address.index}, "
    f"{my_mailing.from_address.city}, {my_mailing.from_address.street}, "
    f"{my_mailing.from_address.house} - {my_mailing.from_address.apartment} "
    f"в {my_mailing.to_address.index}, {my_mailing.to_address.city}, "
    f"{my_mailing.to_address.street}, {my_mailing.to_address.house} - "
    f"{my_mailing.to_address.apartment}. Стоимость {my_mailing.cost} рублей."
)

print(message)
