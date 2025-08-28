import os
from DataLoader import load_data
from Model import train_and_evaluate

DATA_DIR = "data_cleaned"

if __name__ == "__main__":
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

    if not files:
        print("❌ No CSV files found in data_cleaned/")
        exit()

    print("📂 Available stock datasets:")
    for idx, f in enumerate(files, 1):
        print(f"{idx}. {f}")

    choice = int(input("\n👉 Enter the number of the stock you want to train on: "))

    if 1 <= choice <= len(files):
        stock_file = os.path.join(DATA_DIR, files[choice - 1])
        x_train, y_train, x_test, y_test, scaler = load_data(stock_file)
        train_and_evaluate(stock_file, stock_name=files[choice - 1].replace(".csv", ""))


    else:
        print("❌ Invalid choice.")
