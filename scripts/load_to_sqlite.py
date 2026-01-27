import sqlite3
import pandas as pd
from pathlib import Path

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "corporate.db"
DATA_DIR = BASE_DIR / "data"

# -----------------------------
# Connect to SQLite
# -----------------------------
conn = sqlite3.connect(DB_PATH)

print("Connected to SQLite database")

# -----------------------------
# Read CSV files
# -----------------------------
source_df = pd.read_csv(DATA_DIR / "source_transactions.csv")
target_df = pd.read_csv(DATA_DIR / "target_transactions.csv")

# -----------------------------
# Load data into SQLite tables
# -----------------------------
source_df.to_sql(
    "source_transactions",
    conn,
    if_exists="replace",
    index=False
)

target_df.to_sql(
    "target_transactions",
    conn,
    if_exists="replace",
    index=False
)

print("Tables created and data loaded successfully")

# -----------------------------
# Close connection
# -----------------------------
cursor = conn.cursor()

# -----------------------------
# Create data quality rules table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS data_quality_rules (
    rule_id INTEGER PRIMARY KEY,
    rule_name TEXT,
    description TEXT,
    severity TEXT
);
""")

# -----------------------------
# Create data quality results table
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS data_quality_results (
    result_id INTEGER PRIMARY KEY,
    rule_id INTEGER,
    failed_count INTEGER,
    run_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()

conn.close()

