from typing import Any
from utils import database
import time


def get_database_table() -> str:
    return """CREATE TABLE IF NOT EXISTS promocodes (
    id INTEGER PRIMARY KEY,
    name TEXT,
    value INTEGER,
    percent INTEGER,
    uses INTEGER,
    max_uses INTEGER,
    expires INTEGER,
    active INTEGER,
    UNIQUE (name))"""


class Promocode:
    def __init__(self, id: int) -> None:
        self.id = id

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"<Promocode id={self.id} name={self.name}>"

    def __query(self, field: str) -> Any:
        return database.fetch(f"SELECT {field} FROM promocodes WHERE id = ?", (self.id,))

    def __update(self, field: str, value: Any) -> None:
        database.execute(f"UPDATE promocodes SET {field} = ? WHERE id = ?", (value, self.id))

    @property
    def name(self) -> str:
        return self.__query("name")
    @name.setter
    def name(self, value: str) -> None:
        self.__update("name", value)

    @property
    def value(self) -> int:
        return self.__query("value")
    @value.setter
    def value(self, value: int) -> None:
        self.__update("value", value)

    @property
    def percent(self) -> bool:
        return bool(self.__query("percent"))
    @percent.setter
    def percent(self, value: bool) -> None:
        self.__update("percent", int(value))

    @property
    def uses(self) -> int:
        return self.__query("uses")
    @uses.setter
    def uses(self, value: int) -> None:
        self.__update("uses", value)

    @property
    def max_uses(self) -> int:
        return self.__query("max_uses")
    @max_uses.setter
    def max_uses(self, value: int) -> None:
        self.__update("max_uses", value)

    @property
    def expires(self) -> int:
        return self.__query("expires")
    @expires.setter
    def expires(self, value: int) -> None:
        self.__update("expires", value)

    @property
    def active(self) -> bool:
        return bool(self.__query("active"))
    @active.setter
    def active(self, value: bool) -> None:
        self.__update("active", int(value))

    def can_use(self) -> bool:
        return self.active and self.uses < self.max_uses and self.expires > time.time()


def create(
    name: str,
    value: int,
    percent: bool,
    max_uses: int,
    expires: int,
    active: bool
) -> Promocode:
    id = database.fetch(
            "INSERT INTO promocodes (name, value, percent, uses, max_uses, expires, active) VALUES (?, ?, ?, ?, ?, ?, ?)",
            name, value, int(percent), 0, max_uses, expires, int(active)
    )
    return Promocode(id)

