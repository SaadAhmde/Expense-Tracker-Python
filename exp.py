import csv
import os

FILE_NAME = "expenses.csv"


# ---------------- LOAD DATA ----------------
def load_data():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses


# ---------------- SAVE DATA ----------------
def save_data(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "category", "amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)


# ---------------- ADD EXPENSE ----------------
def add_expense(expenses):
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = input("Enter amount: ")

    expenses.append({
        "date": date,
        "category": category,
        "amount": amount
    })

    save_data(expenses)
    print("Expense Added Successfully!")


# ---------------- VIEW EXPENSES ----------------
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    for i, exp in enumerate(expenses):
        print(f"{i}. {exp['date']} | {exp['category']} | {exp['amount']}")


# ---------------- EDIT EXPENSE ----------------
def edit_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter index to edit: "))

    if 0 <= index < len(expenses):
        expenses[index]["date"] = input("New date: ")
        expenses[index]["category"] = input("New category: ")
        expenses[index]["amount"] = input("New amount: ")
        save_data(expenses)
        print("Expense Updated!")
    else:
        print("Invalid index!")


# ---------------- DELETE EXPENSE ----------------
def delete_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter index to delete: "))

    if 0 <= index < len(expenses):
        expenses.pop(index)
        save_data(expenses)
        print("Expense Deleted!")
    else:
        print("Invalid index!")


# ---------------- MAIN MENU ----------------
def main():
    expenses = load_data()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            edit_expense(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
