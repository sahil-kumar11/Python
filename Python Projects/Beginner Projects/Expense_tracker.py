from datetime import date

EXPENSE_FILE = "expenses.txt"

def load_expense():
    try:
        with open(EXPENSE_FILE, "r") as file:
            exp = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        exp = []
    return exp

def save_expense(exp):
    with open(EXPENSE_FILE, "w") as file:
        for expen in exp:
            file.write(expen + "\n")

def add_expense():
    expense_amount = input("Enter your expense amount: ").strip()
    category = input("Enter your category: ").strip()
    today = date.today()  

    exp = load_expense()
    exp.append(f"{expense_amount}, {category}, {today}")  
    save_expense(exp)

    print(f"Added: {expense_amount} ({category}) on {today}")

def view_expense():
    exp = load_expense()
    if not exp:
        print("No expenses yet.")
    else:
        print("\nYour Expense List:")
        for i, expen in enumerate(exp, 1):
            print(f"{i}. {expen}")

def view_total_expense():
    total = 0
    with open(EXPENSE_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(",")  
            if parts:
                try:
                    total += int(parts[0])  
                except ValueError:
                    pass  
    print(f"\nThe Total Expense is: {total}")

def menu():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Exit")

        choice = input("Enter number between 1 to 4: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            view_total_expense()
        elif choice == "4":
            print("Bye Bye")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    menu()
