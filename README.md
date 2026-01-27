# Corporate Data Quality & Reconciliation Framework

## Project Overview

This project is a **corporate-style data quality and reconciliation framework** built using **Python, SQL, and SQLite**. It simulates how real organisations validate and monitor data as it moves between systems.

In many companies, transactional data is created in one system (often called the **source system**) and then copied into another system for reporting or analytics (the **target system**). During this transfer, data issues frequently occur — such as missing records, duplicate records, or mismatched values.  
This project demonstrates how such issues can be **detected, tracked, and governed** in a structured and repeatable way.

---

## Step 1: Input Data (Source vs Target)

The project starts with two CSV files:

- **`source_transactions.csv`** → represents the original system where transactions are created  
- **`target_transactions.csv`** → represents a downstream reporting system  

Both datasets contain realistic transactional fields such as:
- transaction ID  
- account ID  
- amount  
- currency  
- transaction type  
- transaction date  
- status (e.g. `BOOKED`, `CANCELLED`)  

These CSV files act as **raw incoming business data**, similar to files received daily in corporate environments.

---

## Step 2: Load Data into a Database

Instead of analysing CSV files directly, the data is loaded into a **SQLite database** (`corporate.db`).  
SQLite is used as a lightweight relational database to replicate how systems like **PostgreSQL or MySQL** are used in production.

Two database tables are created:

- `source_transactions`
- `target_transactions`

From this point onward:
- **SQL** becomes the primary tool for validation and reconciliation  
- **Python** is used only to orchestrate execution  

This mirrors real-world data pipelines.

---

## Step 3: Define Data Quality Rules (Rule Catalogue)

A dedicated rules table called **`data_quality_rules`** is created to store *what checks should exist*, instead of hardcoding logic directly in scripts.

Each rule includes:
- a rule ID  
- a rule name  
- a description of the business logic  
- a severity level (`HIGH` / `MEDIUM`)  

Example rules include:
- Transaction IDs must be unique in the target system  
- All non-cancelled source transactions must appear in the target  
- Transaction amounts must match between source and target  

This approach reflects **data governance best practices**, where rules are defined separately from execution logic.

---

## Step 4: Execute Controls (SQL-based Reconciliation)

A control execution script runs **SQL queries** to evaluate each rule.  
These queries make use of:

- joins (`INNER JOIN`, `LEFT JOIN`)  
- aggregations (`GROUP BY`, `HAVING`)  
- mismatch comparisons  

The framework checks for:
- duplicate transactions in the target system  
- missing transactions in the target  
- extra transactions not present in the source  
- amount mismatches between systems  
- invalid reporting of cancelled transactions  

---

## Step 5: Store Results with History

Each time the controls are executed, the results are written to a separate table called **`data_quality_results`**.

For every rule execution, the framework stores:
- the rule ID  
- the number of records that failed  
- the timestamp of execution  

This creates a **historical audit trail**, allowing users to:
- analyse trends over time  
- monitor recurring data quality issues  
- demonstrate data quality and control effectiveness  

---

## Step 6: Separation of Responsibilities

The project intentionally separates responsibilities:

- **Python** → automation, orchestration, repeatable execution  
- **SQL** → reconciliation logic and validation  
- **Database** → storage of data, rules, and historical results  

This separation mirrors real corporate data pipelines and improves **maintainability and scalability**.

---

## Why This Project Is Valuable

This project demonstrates practical skills in:

- SQL joins and reconciliation logic  
- Python-driven automation  
- Data quality governance  
- Rule-based system design  
- Auditability and historical tracking  

It reflects how data quality checks are implemented in **financial services**, **analytics teams**, and **enterprise data platforms**.
<!-- README updated -->
