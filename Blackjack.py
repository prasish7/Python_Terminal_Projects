import random 

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
random.shuffle(card)
user_cards = random.sample(card, 2)
computer_cards = random.sample(card, 2)
user_sum = sum(user_cards)
computer_sum = sum(computer_cards)
print (f"{user_cards[0]}, {user_cards[1]} (Total: {user_sum})")
print (f"{computer_cards[0]}, hidden (Total : ?)")
isRunning = True
while isRunning:
    user_choice = input("Do you want to hit or stand? Type 'h' or 's': ")
    if user_choice == 'h':
        new_card = random.choice(card)
        user_cards.append(new_card)
        user_sum = sum(user_cards)
        print (f"Your cards: {user_cards} (Total: {user_sum})")
        if user_sum > 21:
            print("You went over. You lose!")
            isRunning = False
    else:
        while computer_sum < 17:
            new_card = random.choice(card)
            computer_cards.append(new_card)
            computer_sum = sum(computer_cards)
        print (f"Computer's cards: {computer_cards} (Total: {computer_sum})")
        if computer_sum > 21:
            print("Computer went over. You win!")
        elif user_sum > computer_sum:
            print("You win!")
        elif user_sum < computer_sum:
            print("Computer wins!")
        else:
            print("It's a tie!")
        isRunning = False


    