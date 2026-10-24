import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")
    print("\n")

def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]        
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    return all(cell in ['X', 'O'] for cell in board)

def get_available_moves(board):
    return [i for i in range(9) if board[i] not in ['X', 'O']]

def computer_move(board):
    available = get_available_moves(board)

    # Try to win
    for move in available:
        board_copy = board[:]
        board_copy[move] = 'O'
        if check_winner(board_copy, 'O'):
            return move

    # Try to block player
    for move in available:
        board_copy = board[:]
        board_copy[move] = 'X'
        if check_winner(board_copy, 'X'):
            return move

    return random.choice(available)

def play_game(vs_computer=False):
    board = [str(i) for i in range(9)]
    current_player = 'X'
    
    while True:
        clear_screen()
        print_board(board)
        
        if vs_computer and current_player == 'O':
            move = computer_move(board)
            print("Computer is thinking...")
            input("Press Enter to continue...")
        else:
            player_name = "Computer" if vs_computer and current_player == 'O' else f"Player {current_player}"
            try:
                move = int(input(f"{player_name}, enter your move (0-8): "))
                if move not in get_available_moves(board):
                    print("Invalid move! Try again.")
                    input("Press Enter to continue...")
                    continue
            except ValueError:
                print("Please enter a valid number!")
                input("Press Enter to continue...")
                continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            clear_screen()
            print_board(board)
            winner = "Computer" if vs_computer and current_player == 'O' else f"Player {current_player}"
            print(f" {winner} wins!")
            break
        
        if is_board_full(board):
            clear_screen()
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

def main_menu():
    while True:
        clear_screen()
        print("=" * 30)
        print("   TIC-TAC-TOE GAME")
        print("=" * 30)
        print("\n1. Play vs Computer")
        print("2. Play with Friend")
        print("3. Exit")
        print("\n" + "=" * 30)
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            play_game(vs_computer=True)
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            play_game(vs_computer=False)
            input("\nPress Enter to return to menu...")
        elif choice == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please try again.")
            input("Press Enter to continue...")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes' and play_again != 'y' :
          break
        print("Thank you for playing! Goodbye!")
        
if __name__ == "__main__":
    main_menu()