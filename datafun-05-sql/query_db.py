"""
query_db.py
Author: Bakhrom Botirov
Description: Query data from the SQLite database.
"""

import sqlite3
from pathlib import Path

db_file = Path("example.db")

conn = sqlite3.connect(db_file)
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("Students in database:")
for row in rows:
    print(row)

conn.close()
