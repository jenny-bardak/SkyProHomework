import os

from sqlalchemy import create_engine


# берём строку подключения из переменной окружения
# так пароль не хранится прямо в коде
DATABASE_URL = os.getenv("LESSON9_DATABASE_URL")


def get_engine():
    # проверяем, что строка подключения задана
    # без неё тесты не смогут обратиться к базе
    if DATABASE_URL is None:
        raise RuntimeError(
            "задайте переменную окружения "
            "LESSON9_DATABASE_URL"
        )

    # создаём engine для отправки запросов через SQLAlchemy
    return create_engine(DATABASE_URL)
