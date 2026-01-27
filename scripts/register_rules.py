import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

rules = [
    (1, "Duplicate transactions in TARGET",
     "Transaction IDs should be unique in target system", "HIGH"),

    (2, "Missing transactions in TARGET",
     "All non-cancelled source transactions must appear in target", "HIGH"),

    (3, "Extra transactions in TARGET",
     "Target should not contain transactions absent in source", "MEDIUM"),

    (4, "Amount mismatch",
     "Amounts should match between source and target", "HIGH"),

    (5, "Cancelled transactions reported",
     "Cancelled transactions should not appear in target", "MEDIUM")
]

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.executemany("""
INSERT OR REPLACE INTO data_quality_rules (rule_id, rule_name, description, severity)
VALUES (?, ?, ?, ?);
""", rules)

conn.commit()
conn.close()

print(f"✅ Registered {len(rules)} rules into data_quality_rules")

