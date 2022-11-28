from typing import Any
from utils import database

def get_database_table():
    return """CREATE TABLE IF NOT EXISTS items (
id INTEGER PRIMARY KEY,
name TEXT,
description TEXT,
price REAL,
image TEXT,
group_id INTEGER,
is_subscription INTEGER,
is_active INTEGER
)"""


class Item:
    def __init__(self, id: int) -> None:
        self.id = id

    def __query(self, field: str) -> Any:
        return database.fetch("SELECT {} FROM items WHERE id = ?".format(field), (self.id,))[0]

    def __update(self, field: str, value: Any) -> None:
        database.execute("UPDATE items SET {} = ? WHERE id = ?".format(field), (value, self.id))

    def __str__(self) -> str:
        return f"<Item id={self.id} name={self.name}>"

    @property
    def name(self) -> str:
        return self.__query("name")
    @name.setter
    def name(self, value: str) -> None:
        self.__update("name", value)

    @property
    def description(self) -> str:
        return self.__query("description")
    @description.setter
    def description(self, value: str) -> None:
        self.__update("description", value)

    @property
    def price(self) -> float:
        return self.__query("price")
    @price.setter
    def price(self, value: float) -> None:
        self.__update("price", value)

    @property
    def image(self) -> bytes:
        return open(f"images/{self.__query('image')}", "rb").read()
    @image.setter
    def image(self, value: bytes) -> None:
        self.__update("image", value)

    @property
    def group_id(self) -> int:
        return self.__query("group_id")
    @group_id.setter
    def group_id(self, value: int) -> None:
        self.__update("group_id", value)

    @property
    def is_subscription(self) -> bool:
        return bool(self.__query("is_subscription"))
    @is_subscription.setter
    def is_subscription(self, value: bool) -> None:
        self.__update("is_subscription", int(value))

    @property
    def is_active(self) -> bool:
        return bool(self.__query("is_active"))
    @is_active.setter
    def is_active(self, value: bool) -> None:
        self.__update("is_active", int(value))


def get_items() -> list:
    return [Item(id) for id in database.fetch("SELECT id FROM items")]


def create(
    id: int,
    name: str,
    description: str,
    price: float,
    image: bytes,
    group_id: int,
    is_subscription: bool,
    is_active: bool,
) -> Item:
    database.execute(
        "INSERT INTO items VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (id, name, description, price, image, group_id, int(is_subscription), int(is_active))
    )
    return Item(id)

