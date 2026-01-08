import sqlite3

conn = sqlite3.connect("database.db")
conn.executescript(open("schema.sql").read())
conn.close()

print("Database initialized successfully")
