
from pathlib import Path
import pandas as pd
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATABASE = BASE_DIR / "shipment_database.db"

print("=" * 60)
print("WALMART SHIPPING DATA - SCHEMA INSPECTION")
print("=" * 60)

# Inspect spreadsheets
for file in sorted(DATA_DIR.rglob("*.xlsx")):

    df = pd.read_excel(file)

    print(f"\nSpreadsheet: {file.name}")
    print(f"Total rows: {len(df)}")
    print(f"Columns: {df.columns.tolist()}")

    print("\nFirst five records:")
    print(df.head().to_string(index=False))

# Inspect database
print("\n" + "=" * 60)
print("SQLITE DATABASE SCHEMA")
print("=" * 60)

if not DATABASE.is_file():
    raise FileNotFoundError(DATABASE)

with sqlite3.connect(DATABASE) as connection:

    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, sql
        FROM sqlite_master
        WHERE type = 'table'
    """)

    for table_name, schema in cursor.fetchall():

        print(f"\nTable: {table_name}")
        print(schema)

print("\nInspection completed successfully.")
