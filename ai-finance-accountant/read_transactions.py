import pandas as pd

def read_csv_transactions(file_path="data/transactions.csv"):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading transaction file: {e}")
        return pd.DataFrame()  # Return empty DataFrame if error

# Allow running this as a standalone script
if __name__ == "__main__":
    df = read_csv_transactions()

    if not df.empty:
        print("\n🧾 All Transactions:")
        print(df)

        total_income = df[df['Category'] == 'Income']['Amount'].sum()
        total_expense = df[df['Category'] == 'Expense']['Amount'].sum()
        net_balance = total_income + total_expense

        print(f"\n💰 Total Income: ${total_income}")
        print(f"💸 Total Expenses: ${-total_expense}")
        print(f"📊 Net Balance: ${net_balance}")
    else:
        print("No transaction data available.")
