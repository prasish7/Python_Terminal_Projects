import random  

user_card = random.sample(range(1, 11), 2)
computer_card = random.sample(range(1, 11), 2)

if sum(user_card) > sum(computer_card):
    print(f"You win!---------\nYour cards: {user_card} (Total: {sum(user_card)}) vs Computer's cards: {computer_card} (Total: {sum(computer_card)})")
elif sum(user_card) < sum(computer_card):
    print(f"Computer wins!---------\nYour cards: {user_card} (Total: {sum(user_card)}) vs Computer's cards: {computer_card} (Total: {sum(computer_card)})")
else:
    print(f"It's a tie!---------\nYour cards: {user_card} (Total: {sum(user_card)}) vs Computer's cards: {computer_card} (Total: {sum(computer_card)})")

