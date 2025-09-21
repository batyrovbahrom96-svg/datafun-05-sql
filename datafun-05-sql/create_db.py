"""
create_db.py
Author: Bakhrom Botirov
Description: Create a simple SQLite database using Python.
"""

import sqlite3
from pathlib import Path

# Database file
db_file = Path("example.db")

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create a simple table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Insert sample data
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 20))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 22))

# Save changes and close
conn.commit()
conn.close()

print("Database created:", db_file.exists())
