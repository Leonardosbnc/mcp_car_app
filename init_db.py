import sqlite3


conn = sqlite3.connect("database.db")
cursor = conn.cursor()


cursor.execute(
    """
CREATE TABLE IF NOT EXISTS carros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ano INTEGER,
    cor TEXT,
    marca TEXT,
    modelo TEXT,
    tipo_combustivel TEXT,
    tipo_cambio TEXT,
    nome TEXT,
    quilometragem INTEGER,
    num_portas INTEGER,
    motorizacao TEXT,
    preco INTEGER
)
"""
)


conn.commit()
conn.close()
