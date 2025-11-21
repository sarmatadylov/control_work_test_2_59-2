CREATE_ITEM_TABLE = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    bought INTEGER DEFAULT 0
);
"""

INSERT_ITEM = "INSERT INTO items (name, bought) VALUES (?, 0)"

SELECT_ITEMS = "SELECT id, name, bought FROM items"

UPDATE_BOUGHT = "UPDATE items SET bought = ? WHERE id = ?"

DELETE_ITEM = "DELETE FROM items WHERE id = ?" 