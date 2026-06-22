import pandas as pd
import os

# Folder containing CSV files
DATA_PATH = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print(f"\nFound {len(csv_files)} CSV files\n")

# Loop through each CSV file
for file in csv_files:

    file_path = os.path.join(DATA_PATH, file)

    print("=" * 80)
    print(f"DATASET: {file}")

    try:
        # Read CSV
        df = pd.read_csv(file_path)

        # Shape
        print("\nShape:")
        print(df.shape)

        # Data types
        print("\nData Types:")
        print(df.dtypes)

        # First 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Basic anomaly checks
        print("\nAnomaly Checks:")

        missing_values = df.isnull().sum().sum()
        duplicate_rows = df.duplicated().sum()

        print(f"Missing Values: {missing_values}")
        print(f"Duplicate Rows: {duplicate_rows}")

    except Exception as e:
        print(f"Error reading {file}: {e}")

print("\nData ingestion completed.")