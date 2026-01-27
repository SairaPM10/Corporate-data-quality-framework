import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT rule_id, rule_name, severity FROM data_quality_rules ORDER BY rule_id;")
rows = cursor.fetchall()

conn.close()

print("\n=== RULES IN DATABASE ===")
for r in rows:
    print(r)
