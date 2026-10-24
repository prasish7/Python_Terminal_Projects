print ("Welcome to the Metric Conversion Tool!")
print("Select the conversion you would like to perform:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kilometers to Miles")
print("4. Miles to Kilometers")
choice = int(input("Enter the number of your choice (1-4): "))
isRunning = True
while isRunning:
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        isRunning = False
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
        isRunning = False
    elif choice == 3:
        kilometers = float(input("Enter distance in Kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} km is equal to {miles} miles")
        isRunning = False
    elif choice == 4:
        miles = float(input("Enter distance in Miles: "))
        kilometers = miles / 0.621371
        print(f"{miles} miles is equal to {kilometers} km")
        isRunning = False
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
        choice = int(input("Enter the number of your choice (1-4): "))


   
  