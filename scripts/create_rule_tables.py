import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS data_quality_rules (
    rule_id INTEGER PRIMARY KEY,
    rule_name TEXT NOT NULL,
    description TEXT,
    severity TEXT NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS data_quality_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    rule_id INTEGER NOT NULL,
    failed_count INTEGER NOT NULL,
    run_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(rule_id) REFERENCES data_quality_rules(rule_id)
);
""")

conn.commit()
conn.close()

print("✅ Rule tables created: data_quality_rules, data_quality_results")
