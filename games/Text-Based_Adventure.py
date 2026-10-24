isRunning = True

while isRunning:
    print("="*50)
    print("Welcome to the Text-Based Adventure Game!")
    print("="*50)
    player_name = input("Enter your name: ")
    player_choice = input(f"Hello, {player_name}! Do you want to explore the Library or go down to the Dungeon? (Type 'Library' or 'Dungeon'): ").strip().lower()
    if player_choice == 'library':
        print("You enter the Library, filled with ancient books and scrolls.")
        action = input("Do you want to read a book or search for a hidden passage? (Type 'Read' or 'Search'): ").strip().lower()
        if action == 'read':
            print("="*50)
            print("Its a trap. You Lost")
            print("="*50)
        elif action == 'search':
            print("="*50)
            print("You discover a hidden passage that leads to a treasure room. You win!")
            print("="*50)
        else:
            print("Invalid action. Game over.")
    elif player_choice == 'dungeon':
        print("You descend into the dark Dungeon, filled with eerie sounds.")
        action = input("Do you want to fight a monster or look for a treasure chest? (Type 'Fight' or 'Treasure'): ").strip().lower()
        if action == 'fight':
            print("="*50)
            print("You bravely fight the monster and emerge victorious. You win!")
            print("="*50)
        elif action == 'treasure':
            print("="*50)
            print("You lose your way and fall into a pit. You Lost!")
            print("="*50)
        else:
            print("Invalid action. Game over.")

    else:
        print("Invalid choice. Game over.")
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes' and play_again != 'y' :
        isRunning = False
        print("Thank you for playing! Goodbye!")

