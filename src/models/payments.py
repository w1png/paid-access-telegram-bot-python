# this is a class for payments
# id
# user_id
# item_id
# promocode_id
# date_created
# date_paid
# date_expired

from typing import Any
from utils import database
from random import randint
import time


def get_database_table() -> str:
    return """CREATE TABLE IF NOT EXISTS payments (
    id INTEGER,
    user_id INTEGER REFERENCES users(id) NOT NULL,
    item_id INTEGER REFERENCES items(id) NOT NULL,
    promocode_id INTEGER REFERENCES promocodes(id),
    date_created INTEGER NOT NULL,
    date_paid INTEGER,
    date_expired INTEGER"""


class Payment:
    def __init__(self, id: int) -> None:
        self.id = id

    def __str__(self) -> str:
        return f"<Payment id={self.id}>"

    def __query(self, field: str) -> Any:
        return database.fetch(f"SELECT {field} FROM payments WHERE id = ?", (self.id,))

    def __update(self, field: str, value: Any) -> None:
        database.execute(f"UPDATE payments SET {field} = ? WHERE id = ?", (value, self.id))

    @property
    def user_id(self) -> int:
        return self.__query("user_id")

    @property
    def item_id(self) -> int:
        return self.__query("item_id")

    @property
    def promocode_id(self) -> int:
        return self.__query("promocode_id")

    @property
    def date_created(self) -> int:
        return self.__query("date_created")

    @property
    def date_paid(self) -> int:
        return self.__query("date_paid")
    @date_paid.setter
    def date_paid(self, value: int) -> None:
        self.__update("date_paid", value)

    @property
    def date_expired(self) -> int:
        return self.__query("date_expired")
    @date_expired.setter
    def date_expired(self, value: int) -> None:
        self.__update("date_expired", value)


def create(user_id: int, item_id: int, promocode_id: int) -> Payment:
    return database.fetch(
        "INSERT INTO payments VALUES (?, ?, ?, ?, ?, ?, ?)",
        randint(100000, 999999), user_id, item_id, promocode_id, int(time.time()), None, None
    )


