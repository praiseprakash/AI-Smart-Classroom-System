import sqlite3

conn = sqlite3.connect("classroom.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    date TEXT,
    time TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS violations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    violation TEXT,
    date TEXT,
    time TEXT
)
""")

conn.commit()

conn.close()

print("Classroom Database Created")