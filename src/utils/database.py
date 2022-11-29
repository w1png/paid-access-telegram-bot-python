import sqlite3
from typing import Any

def fetch(query, args) -> Any:
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        return cursor.fetchall()

def execute(query, args) -> None:
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()

