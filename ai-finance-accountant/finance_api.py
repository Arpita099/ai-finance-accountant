def process_command(command, transactions=None):
    if transactions is None:
        return "Transaction data is missing."

    command = command.lower()

    if "total income" in command:
        income = transactions[transactions["Category"] == "Income"]["Amount"].sum()
        return f"Your total income is ${income:.2f}."

    elif "total expense" in command or "total spending" in command:
        expense = transactions[transactions["Category"] == "Expense"]["Amount"].sum()
        return f"Your total expenses are ${-expense:.2f}."  # expense is negative

    elif "balance" in command:
        balance = transactions["Amount"].sum()
        return f"Your current balance is ${balance:.2f}."

    elif "summary" in command:
        summary = transactions.groupby("Category")["Amount"].sum()
        response = "Here is your financial summary:\n"
        for category, amount in summary.items():
            response += f"{category}: ${amount:.2f}\n"
        return response.strip()

    elif "transfer" in command:
        return "Transferring $100 to your savings account."

    else:
        return "Sorry, I didn't understand the request."
