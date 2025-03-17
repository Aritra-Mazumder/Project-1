import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

# Load existing expenses from file
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter description: ")
        category = input("Enter category (food, transport, entertainment, etc.): ").lower()
        date = datetime.now().strftime("%Y-%m-%d")
        
        expense = {"amount": amount, "description": description, "category": category, "date": date}
        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

# View all expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    for exp in expenses:
        print(f"{exp['date']} - {exp['category']} - {exp['description']}: ${exp['amount']}")

# View summary by month
def view_monthly_summary():
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        month = exp["date"][:7]  # Extract YYYY-MM
        summary[month] = summary.get(month, 0) + exp["amount"]
    for month, total in summary.items():
        print(f"{month}: ${total:.2f}")

# View expenses by category
def view_category_summary():
    expenses = load_expenses()
    category_summary = {}
    for exp in expenses:
        category = exp["category"]
        category_summary[category] = category_summary.get(category, 0) + exp["amount"]
    for category, total in category_summary.items():
        print(f"{category.capitalize()}: ${total:.2f}")

# Main menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Monthly Summary")
        print("4. View Category Summary")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_monthly_summary()
        elif choice == "4":
            view_category_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
