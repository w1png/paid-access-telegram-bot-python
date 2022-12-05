from typing import Any
from utils import database
from models import promocodes

def get_database_table() -> str:
    return """CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    is_admin INTEGER,
    promocode_id INTEGER, FOREIGN KEY (promocode_id) REFERENCES promocodes(id)
)"""


class User:
    def __init__(self, user_id: int) -> None:
        self.id = user_id
        if not does_exist(self.id):
            create(self.id)

    def __query(self, field: str) -> Any:
        return database.fetch(f"SELECT {field} FROM users WHERE id = ?", (self.id,))

    def __update(self, field: str, value: Any) -> None:
        database.execute(f"UPDATE users SET {field} = ? WHERE id = ?", (value, self.id,))

    @property
    def is_admin(self) -> bool:
        return bool(self.__query("is_admin"))
    @is_admin.setter
    def is_admin(self, value: bool) -> None:
        self.__update("is_admin", int(value))

    @property
    def promocode(self) -> promocodes.Promocode:
        return promocodes.Promocode(self.__query("promocode"))
    @promocode.setter
    def promocode(self, value: promocodes.Promocode) -> None:
        self.__update("promocode", value.id)


def create(user_id: int, is_admin: bool=False) -> User:
    database.execute("INSERT INTO users (id, is_admin, promocode_id) VALUES (?, ?, ?)", (user_id, int(is_admin), None,))
    return User(user_id)


def does_exist(user_id: int) -> bool:
    return bool(database.fetch("SELECT id FROM users WHERE id = ?", (user_id,)))
