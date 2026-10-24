import random
print("Welcome to 'Guess My Number'!")
print("I have selected a number between 1 and 100.")
print("Try to guess the number!")
attempts = 0

secret_number = random.randint(1, 100)
isRunning = True
while isRunning:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100. Please try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} correctly!")
        isRunning = False

print(f"You took {attempts} attempts to guess the number.")