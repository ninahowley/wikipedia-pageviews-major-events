import sqlite3
from datetime import datetime
from typing import List

def init_db():
    conn = sqlite3.connect("raw_data.db")
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS pageviews''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pageviews (
            date TEXT,
            country TEXT,
            search_id INTEGER,
            search_key TEXT,
            view_count INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def insert_data(
    date: str,
    country: str,
    search_id: int,
    search_key: str,
    view_count: int
):
    conn = sqlite3.connect("raw_data.db")
    cursor = conn.cursor()
    
    cursor.execute('''
            INSERT INTO pageviews (date, country, search_id, search_key, view_count)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, country, search_id, search_key, view_count))

    conn.commit()
    conn.close()