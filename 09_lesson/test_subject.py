from sqlalchemy import text

from db import get_engine


# создаём engine один раз для всего файла
# через него каждый тест обращается к базе
engine = get_engine()

# используем большой id для тестовой записи
# так мы не пересекаемся с учебными предметами
TEST_SUBJECT_ID = 9001

# используем узнаваемое название тестового предмета
TEST_SUBJECT_TITLE = "lesson9 test subject"

# это название нужно для проверки изменения
UPDATED_SUBJECT_TITLE = "lesson9 updated subject"


def delete_test_subject(subject_id=TEST_SUBJECT_ID):
    # открываем короткое подключение к базе
    # после запроса оно закроется автоматически
    with engine.begin() as connection:
        # удаляем только нашу тестовую запись
        # настоящие данные остаются нетронутыми
        connection.execute(
            text("delete from subject where subject_id = :subject_id"),
            {"subject_id": subject_id},
        )


def get_subject_by_id(subject_id=TEST_SUBJECT_ID):
    # открываем подключение для чтения таблицы subject
    with engine.connect() as connection:
        # выбираем одну строку по тестовому id
        result = connection.execute(
            text(
                "select subject_id, subject_title "
                "from subject "
                "where subject_id = :subject_id"
            ),
            {"subject_id": subject_id},
        )

        # возвращаем строку или None, если строки нет
        return result.fetchone()


def test_add_subject():
    # заранее очищаем тестовую запись
    # повторный запуск начнётся с того же состояния
    delete_test_subject()

    try:
        # добавляем новый предмет в таблицу
        with engine.begin() as connection:
            connection.execute(
                text(
                    "insert into subject (subject_id, subject_title) "
                    "values (:subject_id, :subject_title)"
                ),
                {
                    "subject_id": TEST_SUBJECT_ID,
                    "subject_title": TEST_SUBJECT_TITLE,
                },
            )

        # читаем добавленную запись из базы
        created_subject = get_subject_by_id()

        # проверяем, что запись появилась
        assert created_subject is not None

        # проверяем сохранённый id
        assert created_subject.subject_id == TEST_SUBJECT_ID

        # проверяем сохранённое название
        assert created_subject.subject_title == TEST_SUBJECT_TITLE
    finally:
        # удаляем тестовую запись даже при падении проверки
        delete_test_subject()


def test_update_subject():
    # заранее очищаем тестовую запись
    # тест не должен зависеть от прошлых запусков
    delete_test_subject()

    try:
        # создаём запись для будущего изменения
        with engine.begin() as connection:
            connection.execute(
                text(
                    "insert into subject (subject_id, subject_title) "
                    "values (:subject_id, :subject_title)"
                ),
                {
                    "subject_id": TEST_SUBJECT_ID,
                    "subject_title": TEST_SUBJECT_TITLE,
                },
            )

            # меняем название через update-запрос
            connection.execute(
                text(
                    "update subject "
                    "set subject_title = :subject_title "
                    "where subject_id = :subject_id"
                ),
                {
                    "subject_id": TEST_SUBJECT_ID,
                    "subject_title": UPDATED_SUBJECT_TITLE,
                },
            )

        # читаем изменённую запись из базы
        updated_subject = get_subject_by_id()

        # проверяем, что запись всё ещё существует
        assert updated_subject is not None

        # проверяем, что название изменилось
        assert updated_subject.subject_title == UPDATED_SUBJECT_TITLE
    finally:
        # удаляем тестовую запись после проверки
        delete_test_subject()


def test_delete_subject():
    # заранее очищаем тестовую запись
    # так при повторном запуске не будет дублей
    delete_test_subject()

    # создаём запись для удаления
    with engine.begin() as connection:
        connection.execute(
            text(
                "insert into subject (subject_id, subject_title) "
                "values (:subject_id, :subject_title)"
            ),
            {
                "subject_id": TEST_SUBJECT_ID,
                "subject_title": TEST_SUBJECT_TITLE,
            },
        )

    # удаляем созданный предмет
    delete_test_subject()

    # пытаемся найти удалённый предмет
    deleted_subject = get_subject_by_id()

    # проверяем, что запись больше не находится
    assert deleted_subject is None
