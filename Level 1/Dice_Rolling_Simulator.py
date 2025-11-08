import random 
 
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

total = dice1 + dice2
print(f"You rolled {dice1} in dice 1 and a {dice2} in dice 2. Total: {total}")