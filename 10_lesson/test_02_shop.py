# импортируем allure для описания теста и шагов отчета
import allure

# импортируем webdriver для запуска браузера
from selenium import webdriver

# импортируем page object классы страниц магазина
from pages import CartPage, CheckoutPage, LoginPage, ShopPage


# название теста в allure-отчете
@allure.title("Проверка итоговой суммы заказа в интернет-магазине")
# описание теста в allure-отчете
@allure.description(
    "Тест авторизуется на сайте Sauce Demo, добавляет три товара "
    "в корзину, оформляет заказ и проверяет итоговую стоимость."
)
# функциональность, к которой относится тест
@allure.feature("Интернет-магазин")
# критичность теста в отчете
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_purchase() -> None:
    """проверяет покупку товаров и итоговую сумму заказа"""
    # запускаем браузер firefox
    driver = webdriver.Firefox()

    try:
        # создаем объект страницы авторизации
        login_page = LoginPage(driver)

        # создаем объект страницы каталога
        shop_page = ShopPage(driver)

        # создаем объект страницы корзины
        cart_page = CartPage(driver)

        # создаем объект страницы оформления заказа
        checkout_page = CheckoutPage(driver)

        # фиксируем шаг открытия страницы в allure-отчете
        with allure.step("Открыть страницу авторизации магазина"):
            # открываем страницу авторизации
            login_page.open()

        # фиксируем шаг авторизации в allure-отчете
        with allure.step("Авторизоваться стандартным пользователем"):
            # вводим логин и пароль стандартного пользователя
            login_page.login("standard_user", "secret_sauce")

        # фиксируем шаг добавления товаров в allure-отчете
        with allure.step("Добавить в корзину три товара"):
            # добавляем товары в корзину
            shop_page.add_items()

        # фиксируем шаг перехода в корзину в allure-отчете
        with allure.step("Перейти в корзину"):
            # открываем корзину
            shop_page.go_to_cart()

        # фиксируем шаг начала оформления заказа в allure-отчете
        with allure.step("Начать оформление заказа"):
            # нажимаем checkout
            cart_page.checkout()

        # фиксируем шаг заполнения формы в allure-отчете
        with allure.step("Заполнить данные покупателя"):
            # заполняем имя, фамилию и почтовый индекс
            checkout_page.fill_form("Jenny", "Bardak", "123456")

        # фиксируем шаг получения суммы в allure-отчете
        with allure.step("Получить итоговую стоимость заказа"):
            # получаем итоговую сумму со страницы
            total_price = checkout_page.get_total()

        # фиксируем шаг проверки суммы в allure-отчете
        with allure.step("Проверить, что итоговая стоимость равна $58.29"):
            # проверяем, что фактическая сумма равна ожидаемой
            assert total_price == "$58.29"
    finally:
        # закрываем браузер после теста
        driver.quit()
