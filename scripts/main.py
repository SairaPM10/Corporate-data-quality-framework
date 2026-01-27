import pandas as pd
from pathlib import Path

# -----------------------------
# Load data
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

source_df = pd.read_csv(BASE_DIR / "data" / "source_transactions.csv")
target_df = pd.read_csv(BASE_DIR / "data" / "target_transactions.csv")

# -----------------------------
# Remove cancelled transactions from source
# -----------------------------
source_df = source_df[source_df["status"] != "CANCELLED"]

# -----------------------------
# Duplicate check
# -----------------------------
duplicate_target = target_df[target_df.duplicated(subset=["transaction_id"], keep=False)]

# -----------------------------
# Reconciliation
# -----------------------------
merged = source_df.merge(
    target_df,
    on="transaction_id",
    how="outer",
    suffixes=("_source", "_target"),
    indicator=True
)

# Missing / Extra
missing_in_target = merged[merged["_merge"] == "left_only"]
extra_in_target = merged[merged["_merge"] == "right_only"]

# Matched records
matched = merged[merged["_merge"] == "both"]

# Amount mismatch
amount_mismatch = matched[
    matched["amount_source"] != matched["amount_target"]
]

# Clean matches
clean_matches = matched[
    matched["amount_source"] == matched["amount_target"]
]

# -----------------------------
# Output summary
# -----------------------------
print("\n====== RECONCILIATION SUMMARY ======")
print(f"Total source records: {len(source_df)}")
print(f"Total target records: {len(target_df)}")
print(f"Duplicate transactions in TARGET: {len(duplicate_target)}")
print(f"Missing in TARGET: {len(missing_in_target)}")
print(f"Extra in TARGET: {len(extra_in_target)}")
print(f"Amount mismatches: {len(amount_mismatch)}")
print(f"Clean matched records: {len(clean_matches)}")


