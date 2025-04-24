import sqlite3
import os

DB_PATH = os.path.join('database', 'biblioteca.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        os.makedirs('database', exist_ok=True)
        conn = get_db_connection()
        conn.execute('./library_tables.sql')
        conn.commit()
        conn.close()
