from typing import Any
from utils import database
import promocodes

def get_database_table() -> str:
    return """CREATE TABLE IF NOT EXISTS users (
    id INTEGER,
    promocode FOREIGN KEY REFERENCES promocodes(id),"""


class User:
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def __query(self, field: str) -> Any:
        return database.fetch(f"SELECT {field} FROM users WHERE id = ?", (self.user_id,))

    def __update(self, field: str, value: Any) -> None:
        database.execute(f"UPDATE users SET {field} = ? WHERE id = ?", (value, self.user_id))

    @property
    def promocode(self) -> promocodes.Promocode:
        return promocodes.Promocode(self.__query("promocode"))
    @promocode.setter
    def promocode(self, value: promocodes.Promocode) -> None:
        self.__update("promocode", value.id)


def create(user_id: int) -> None:
    database.execute("INSERT INTO users (id, promocode) VALUES (?, ?)", (user_id, None))

