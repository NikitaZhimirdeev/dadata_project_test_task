import sqlite3

class SQLighter:

    # Подключаемся к БД и сохраняем курсор соединения
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # Создаем необходимую таблицу если ее нет
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_data(
        login TEXT,
        password TEXT,
        API_key TEXT,
        secret TEXT,
        lang TEXT)
        """)
        self.connection.commit()

    # Проверка на существование логина
    def login_verification(self, login):
        # with self.connection:
        result = self.cursor.execute("""SELECT * FROM users_data WHERE login = ?""",(login,)).fetchall()
        return bool(len(result))

    # Добавляем данные о пользователе в БД
    def add_user(self, login, password, API_key, secret, lang):
        self.cursor.execute("""INSERT INTO users_data VALUES (?, ?, ?, ?, ?)""", (login, password, API_key, secret, lang))
        self.connection.commit()

    # Проверка на существование логина
    def login_v(self, login):
        # with self.connection:
        result = self.cursor.execute("""SELECT * FROM users_data WHERE login = ?""", (login,)).fetchall()
        return result
