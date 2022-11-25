import sqlite3

def fetch(query, *args) -> list:
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        return cursor.fetchall()

def execute(query, *args) -> None:
    with sqlite3.connect("database.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()

