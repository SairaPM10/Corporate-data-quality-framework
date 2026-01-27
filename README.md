# Corporate Data Quality & Reconciliation Framework

## Overview
This project demonstrates a rule-based data quality and reconciliation framework using Python and SQL (SQLite).

It simulates how corporate data teams validate transactional data between a source system and a reporting system.

## Key Features
- SQL-based reconciliation (duplicates, missing, extra, mismatched records)
- Rule catalogue with severity levels
- Control execution engine
- Historical tracking of data quality results
- Separation of concerns: SQL for logic, Python for orchestration

## Tech Stack
- Python
- SQLite
- SQL
- Pandas

## Project Structure
- data/ : sample transactional data (dummy)
- db/ : SQLite database
- scripts/ : ingestion, validation, reconciliation logic

## Use Case
Designed to mirror real-world data quality checks used in banks, asset managers, and analytics teams.

## How to Run
1. Load data into SQLite:
   ```bash
   python scripts/load_to_sqlite.py
