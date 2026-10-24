import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "bank_data.json"
balance = 0
deposit = 0
withdraw = 0

def save_data():
    with open(DATA_FILE, 'w') as file:
        data = {'balance': balance, 'deposit': deposit, 'withdraw': withdraw}
        json.dump(data, file)
try:
    with open(DATA_FILE, 'r') as file:
        data = json.load(file)
        balance = data.get('balance', 0)
        deposit = data.get('deposit', 0)
        withdraw = data.get('withdraw', 0)
except FileNotFoundError:
    balance = 0
    deposit = 0
    withdraw = 0


isRunning = True
while isRunning:
    print("Welcome to the Bank Account Program")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Please select an option (1-4): "))

    if choice == 1:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            deposit += amount
            balance += amount
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid amount. Please enter a positive number.")

    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            withdraw += amount
            balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")

    elif choice == 3:
        print(f"Current Balance: ${balance}")
        print(f"Total Deposited: ${deposit}")
        print(f"Total Withdrawn: ${withdraw}")

    elif choice == 4:
        
        with open(DATA_FILE, 'w') as file:
            data = {'balance': balance, 'deposit': deposit, 'withdraw': withdraw}
            json.dump(data, file)
        isRunning = False
        print("Thank you for using the Bank Account Program. Goodbye!")

    else:
        print("Invalid option. Please select a number between 1 and 4.")
