import sqlite3
from typing import Any

def fetch(query, args=None) -> Any:
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args or ())
        return cursor.fetchall()

def execute(query, args=None) -> None:
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args or ())
        connection.commit()

