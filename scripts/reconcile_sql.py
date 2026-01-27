import sqlite3
from pathlib import Path

# -----------------------------
# Connect to database
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("\n====== SQL RECONCILIATION RESULTS ======\n")

# -----------------------------
# 1. Duplicate transactions in TARGET
# -----------------------------
print("1️⃣ Duplicate transactions in TARGET")

cursor.execute("""
SELECT transaction_id, COUNT(*) AS cnt
FROM target_transactions
GROUP BY transaction_id
HAVING COUNT(*) > 1;
""")

duplicates = cursor.fetchall()
print(duplicates if duplicates else "No duplicates found")

# -----------------------------
# 2. Missing in TARGET
# -----------------------------
print("\n2️⃣ Missing transactions in TARGET")

cursor.execute("""
SELECT s.transaction_id
FROM source_transactions s
LEFT JOIN target_transactions t
ON s.transaction_id = t.transaction_id
WHERE t.transaction_id IS NULL
AND s.status != 'CANCELLED';
""")

missing = cursor.fetchall()
print(missing if missing else "No missing transactions")

# -----------------------------
# 3. Extra in TARGET
# -----------------------------
print("\n3️⃣ Extra transactions in TARGET")

cursor.execute("""
SELECT t.transaction_id
FROM target_transactions t
LEFT JOIN source_transactions s
ON t.transaction_id = s.transaction_id
WHERE s.transaction_id IS NULL;
""")

extra = cursor.fetchall()
print(extra if extra else "No extra transactions")

# -----------------------------
# 4. Amount mismatches
# -----------------------------
print("\n4️⃣ Amount mismatches")

cursor.execute("""
SELECT
    s.transaction_id,
    s.amount AS source_amount,
    t.amount AS target_amount
FROM source_transactions s
JOIN target_transactions t
ON s.transaction_id = t.transaction_id
WHERE s.amount != t.amount
AND s.status != 'CANCELLED';
""")

mismatches = cursor.fetchall()
print(mismatches if mismatches else "No mismatches found")

# -----------------------------
# 5. Clean matched records
# -----------------------------
print("\n5️⃣ Clean matched transactions")

cursor.execute("""
SELECT
    s.transaction_id
FROM source_transactions s
JOIN target_transactions t
ON s.transaction_id = t.transaction_id
WHERE s.amount = t.amount
AND s.status != 'CANCELLED';
""")

clean = cursor.fetchall()
print(clean if clean else "No clean matches")

# -----------------------------
# Close connection
# -----------------------------
conn.close()
