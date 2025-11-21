import sqlite3
from db import queries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    print("База данных подключена")

    cursor.execute(queries.CREATE_ITEM_TABLE)
    conn.commit()
    conn.close()


def add_item(name):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(queries.INSERT_ITEM, (name,))
    conn.commit()

    item_id = cursor.lastrowid
    conn.close()

    return item_id


def get_items():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(queries.SELECT_ITEMS)
    items = cursor.fetchall()

    conn.close()
    return items


def set_bought(item_id, value):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(queries.UPDATE_BOUGHT, (value, item_id))
    conn.commit()

    conn.close()


def delete_item(item_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    cursor.execute(queries.DELETE_ITEM, (item_id,))
    conn.commit()

    conn.close()