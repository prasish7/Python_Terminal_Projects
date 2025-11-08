import random 
user_input = input("Choose Truth or Dare (T/D): ").upper()
isRunning = True

while isRunning:
    if user_input == "Truth" or user_input == 'T' or user_input == 't':
        truth_questions = [
            "What is your biggest fear?",
            "Have you ever lied to your best friend?",
            "What is your most embarrassing moment?",
            "What is a secret you have never told anyone?",
            "Who was your first crush?"
        ]
        print("Truth Question: " + random.choice(truth_questions))
        answer = input("Your answer: ")
        print("Thank you for your honesty! Your answer: " + answer)
    elif user_input == "Dare" or user_input == 'D' or user_input == 'd':
        dare_tasks = [
            "Do 10 push-ups.",
            "Sing a song loudly.",
            "Dance for 30 seconds.",
            "Do an impression of your favorite celebrity.",
            "Wear a funny hat for the next hour."
        ]
        print("Dare Task: " + random.choice(dare_tasks))
        answer = input("Your answer: ").strip().upper()
        print("You completed the dare! your answer: " + answer)
    else:
        print("Invalid choice. Please choose either 'T' for Truth or 'D' for Dare.")

    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again == 'Y' or play_again == 'y':
        user_input = input("Choose Truth or Dare (T/D): ").upper()
        choices = ["Truth", "Dare"]
        choice = random.choice(choices)
        print(f"You got: {choice}")

    else:
        isRunning = False
        print("Thanks for playing!")






