import sqlite3

CONN = sqlite3.connect('library_books.db')
CURSOR = CONN.cursor()