import csv
import datetime

expense = []

def add_exp():
    date_str = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date_str:
        date = datetime.date.today()
    else:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    
    expense.append({
        "date": date,
        "amount": amount,
        "category": category,
       
    })
def view_exp():
    if not expense:
        print("No expenses recorded.")
        return
    print("\n--- Expenses ---")
    for exp in expense:
        print(f"Date: {exp['date']}, Amount: {exp['amount']}, Category: {exp['category']}")

def view_total_exp():
    if not expense:
        print("No expenses recorded.")
        return
    total = sum(exp['amount'] for exp in expense)
    print(f"\nTotal Expenses: {total}")

def save_file():
    with open("expenses.csv", "w", newline="") as csvfile:
        fieldnames = ["date", "amount", "category"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for exp in expense:
            writer.writerow(exp)

def load_file():
    try:
        with open("expenses.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            expense = []
            for row in reader:
                row['date'] = datetime.datetime.strptime(row['date'], "%Y-%m-%d").date()
                row['amount'] = float(row['amount'])
                expense.append(row)
    except FileNotFoundError:
        expense = []

def main():
    load_file()
    while True :
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Save & Exit\n")
        choice = int(input("Enter between 1-4:  "))
        if choice == 1:
            add_exp()
        elif choice == 2:
            view_exp()
        elif choice == 3:
            view_total_exp()
        elif choice == 4:
            save_file()
            break
        else:
            print("Invalid\n")

if __name__ == "__main__":
    main()