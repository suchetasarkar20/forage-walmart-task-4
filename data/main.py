
from pathlib import Path
import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE = BASE_DIR / "shipment_database.db"

print("=" * 60)
print("WALMART SHIPPING DATA - SCHEMA INSPECTION")
print("=" * 60)

# Inspect all spreadsheet files
for file in sorted(DATA_DIR.rglob("*")):

    if file.suffix.lower() not in [".xlsx", ".xls", ".csv"]:
        continue

    print(f"\nSpreadsheet: {file.name}")

    if file.suffix.lower() == ".csv":
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    print(f"Total rows: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")

    print("\nFirst five records:")
    print(df.head().to_string(index=False))

# Inspect SQLite database
print("\n" + "=" * 60)
print("SQLITE DATABASE SCHEMA")
print("=" * 60)

if not DATABASE.is_file():
    raise FileNotFoundError(DATABASE)

connection = sqlite3.connect(DATABASE)

try:
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, sql
        FROM sqlite_master
        WHERE type = 'table'
    """)

    for table_name, schema in cursor.fetchall():

        print(f"\nTable: {table_name}")
        print(schema)

finally:
    connection.close()

print("\nInspection completed successfully.")
