# Основной модуль: отвечает за запуск и управление браузером
# (в данном случае Firefox)
from selenium import webdriver
# Импортируем все классы страниц, которые мы описали в файле pages.py
from pages import LoginPage, ShopPage, CartPage, CheckoutPage


# ГЛАВНЫЙ ТЕСТ: проверяет покупку товаров в магазине
def test_shop_purchase():
    # Создаем экземпляр браузера Firefox
    driver = webdriver.Firefox()

    # Создаем объекты страниц. Каждый из них "запоминает" наш браузер (driver)
    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Команда странице: запустить браузер и перейти на сайт магазина
    login_page.open()

    # Вызываем метод авторизации (передаем логин и пароль)
    login_page.login("standard_user", "secret_sauce")

    # Вызываем метод добавления трех нужных товаров в корзину
    shop_page.add_items()

    # Команда странице: нажать на иконку корзины и перейти в неё
    shop_page.go_to_cart()

    # В корзине вызываем метод нажатия на кнопку "Checkout"
    cart_page.checkout()

    # Вызываем метод заполнения формы (передаем имя, фамилию и индекс)
    checkout_page.fill_form("Jenny", "Bardak", "123456")

    # Вызываем метод, который считывает итоговую цену со страницы
    total_price = checkout_page.get_total()

    # ПРОВЕРКА (Assert): сравниваем полученную цену с ожидаемой "$58.29"
    assert total_price == "$58.29"

    # Завершаем работу: закрываем браузер
    driver.quit()
