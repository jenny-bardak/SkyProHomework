from sqlalchemy import create_engine


# сохраняем строку подключения в одном месте
# так её легко заменить, если база будет другой
DATABASE_URL = "postgresql://postgres:Aa123456@localhost:5432/postgres"


def get_engine():
    # создаём engine для отправки запросов через SQLAlchemy
    return create_engine(DATABASE_URL)
