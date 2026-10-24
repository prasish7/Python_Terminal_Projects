

user_input = input("Enter what you want to calculate (Money or Rides): ").strip().lower()
balance = float(input("Enter your MetroCard balance: $"))
if user_input == "money":
    ride_cost = 2.90
    rides = int(balance // ride_cost)
    print(f"With a balance of ${balance:.2f}, you can take {rides} rides.")
elif user_input == "rides":
    rides = int(input("Enter the number of rides you want to take: "))
    ride_cost = 2.90
    total_cost = rides * ride_cost
    if total_cost > balance:
        print(f"You do not have enough balance for {rides} rides. You need ${total_cost - balance:.2f} more.")
    else:
        new_balance = balance - total_cost
        print(f"After taking {rides} rides, your new balance will be ${new_balance:.2f}.")
else:
    print("Invalid input. Please enter 'Money' or 'Rides'.")
