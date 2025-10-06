import sqlite3
from datetime import datetime
from typing import List

def init_pageviews():
    """
    Initialize pageviews table.
    """
    conn = sqlite3.connect("raw_data.db")
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS pageviews''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pageviews (
            date TEXT,
            search_id INTEGER,
            search_key TEXT,
            view_count INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def init_searchkeys():
    """
    Initialize searchkeys table.
    """
    conn = sqlite3.connect("raw_data.db")
    cursor = conn.cursor()

    cursor.execute('''DROP TABLE IF EXISTS searchkeys''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS searchkeys (
            search_key TEXT,
            nature TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_pageview_data(
        
    date: str,
    search_id: int,
    search_key: str,
    view_count: int
):
    """
    Insert rows into pageview table.
    """
    conn = sqlite3.connect("raw_data.db")
    cursor = conn.cursor()
    
    cursor.execute('''
            INSERT INTO pageviews (date, search_id, search_key, view_count)
            VALUES (?, ?, ?, ?)
        ''', (date, search_id, search_key, view_count))

    conn.commit()
    conn.close()

def insert_searchkey_nature(
    search_key: str,
    nature: str
):
    """
    Insert rows into searchkey table.
    """
    conn = sqlite3.connect("raw_data.db")
    cursor = conn.cursor()
    
    cursor.execute('''
            INSERT INTO searchkeys (search_key, nature)
            VALUES (?, ?)
        ''', (search_key, nature))

    conn.commit()
    conn.close()