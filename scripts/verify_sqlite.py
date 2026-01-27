import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("\nTables in database:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

print("\nSample data from source_transactions:")
cursor.execute("SELECT * FROM source_transactions LIMIT 5;")
for row in cursor.fetchall():
    print(row)

conn.close()
