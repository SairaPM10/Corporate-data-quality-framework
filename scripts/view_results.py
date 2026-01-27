import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT
    r.rule_name,
    r.severity,
    res.failed_count,
    res.run_timestamp
FROM data_quality_results res
JOIN data_quality_rules r
ON res.rule_id = r.rule_id
ORDER BY res.run_timestamp DESC;
""")

rows = cursor.fetchall()
conn.close()

print("\n=== DATA QUALITY RESULTS ===")
for row in rows:
    print(row)
