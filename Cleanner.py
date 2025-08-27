import pandas as pd
import os

input_folder = "data/"
output_folder = "data_cleaned/"
os.makedirs(output_folder, exist_ok=True)

files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

for file in files:
    print(f"Cleaning {file}...")

    # Read CSV
    df = pd.read_csv(os.path.join(input_folder, file))

    # Keep only numeric columns relevant for LSTM
    columns_to_keep = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df[[c for c in columns_to_keep if c in df.columns]]

    # Fill missing Close values
    if 'Close' in df.columns:
        df['Close'] = df['Close'].fillna(method='ffill')

    # Drop any remaining NaNs
    df = df.dropna().reset_index(drop=True)

    # Save cleaned CSV
    df.to_csv(os.path.join(output_folder, file), index=False)
    print(f"{file} cleaned and saved to {output_folder}")

print("All files cleaned without using Date column!")
