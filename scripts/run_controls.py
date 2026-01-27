import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("\n=== RUNNING DATA QUALITY CONTROLS ===\n")

# Rule 1: Duplicate transactions in TARGET
cursor.execute("""
SELECT COUNT(*) FROM (
    SELECT transaction_id
    FROM target_transactions
    GROUP BY transaction_id
    HAVING COUNT(*) > 1
);
""")
failed = cursor.fetchone()[0]
cursor.execute(
    "INSERT INTO data_quality_results (rule_id, failed_count) VALUES (?, ?)",
    (1, failed)
)

# Rule 2: Missing in TARGET
cursor.execute("""
SELECT COUNT(*)
FROM source_transactions s
LEFT JOIN target_transactions t
ON s.transaction_id = t.transaction_id
WHERE t.transaction_id IS NULL
AND s.status != 'CANCELLED';
""")
failed = cursor.fetchone()[0]
cursor.execute(
    "INSERT INTO data_quality_results (rule_id, failed_count) VALUES (?, ?)",
    (2, failed)
)

# Rule 3: Extra in TARGET
cursor.execute("""
SELECT COUNT(*)
FROM target_transactions t
LEFT JOIN source_transactions s
ON t.transaction_id = s.transaction_id
WHERE s.transaction_id IS NULL;
""")
failed = cursor.fetchone()[0]
cursor.execute(
    "INSERT INTO data_quality_results (rule_id, failed_count) VALUES (?, ?)",
    (3, failed)
)

# Rule 4: Amount mismatch
cursor.execute("""
SELECT COUNT(*)
FROM source_transactions s
JOIN target_transactions t
ON s.transaction_id = t.transaction_id
WHERE s.amount != t.amount
AND s.status != 'CANCELLED';
""")
failed = cursor.fetchone()[0]
cursor.execute(
    "INSERT INTO data_quality_results (rule_id, failed_count) VALUES (?, ?)",
    (4, failed)
)

conn.commit()
conn.close()

print("Data quality controls executed and results stored")
