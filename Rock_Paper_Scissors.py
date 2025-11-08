import random

user_point = 0 
computer_point = 0
choices = ["rock", "paper", "scissors"]
rounds = int(input("Enter number of rounds you want to play: "))

while rounds > 0 :
    print("------------------------------------------------------------------------")
    user_choice = input("Enter your choice rock , paper, scissors : ").lower()
    print("------------------------------------------------------------------------")
    
    if user_choice not in choices:
        print("Invalid choice, please choose again.")
        continue
    user_choice = user_choice.lower()
    print(f"User choice is : {user_choice}")
    computer_choice = random.choices(choices)
    computer_choice = computer_choice[0]
    print("----------------------------------------")
    print(f"Computer choice is : {computer_choice}")
    print("----------------------------------------")
    if user_choice == computer_choice:
        print("Tie")
    elif (computer_choice == 'rock' and user_choice == 'paper' or \
          computer_choice == 'paper' and user_choice == 'scissors' or \
          computer_choice == 'scissors' and user_choice == 'rock'     ):
        print("User win")
        user_point +=1
    else :
        print("computer win")
        computer_point += 1


    rounds -= 1 
print("----------------------------------------")
print(f"User points : {user_point}")
print("----------------------------------------")
print("----------------------------------------")
print(f"Computer points : {computer_point}")
print("----------------------------------------")
if user_point > computer_point:
    print("----------------------------------------")
    print(" User win")
    print("----------------------------------------")
elif computer_point > user_point:
    print("----------------------------------------")
    print(" Computer win")
    print("----------------------------------------")
else:
    print("----------------------------------------")
    print(" Tie")
    print("----------------------------------------")
