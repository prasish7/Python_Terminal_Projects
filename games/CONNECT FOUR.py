"""A two-player terminal implementation of Connect Four."""

ROWS = 6
COLUMNS = 7
EMPTY = " "
TOKENS = ("X", "O")


def create_board():
    return [[EMPTY for _ in range(COLUMNS)] for _ in range(ROWS)]


def display_board(board):
    print("\n  " + "   ".join(str(column) for column in range(1, COLUMNS + 1)))
    for row in board:
        print("| " + " | ".join(row) + " |")
    print("+" + "---+" * COLUMNS)


def drop_piece(board, column, token):
    if not 0 <= column < COLUMNS:
        return False
    for row in range(ROWS - 1, -1, -1):
        if board[row][column] == EMPTY:
            board[row][column] = token
            return True
    return False


def has_won(board, token):
    directions = ((0, 1), (1, 0), (1, 1), (1, -1))
    for row in range(ROWS):
        for column in range(COLUMNS):
            if board[row][column] != token:
                continue
            for row_step, column_step in directions:
                end_row = row + row_step * 3
                end_column = column + column_step * 3
                if not (0 <= end_row < ROWS and 0 <= end_column < COLUMNS):
                    continue
                if all(
                    board[row + row_step * offset][column + column_step * offset] == token
                    for offset in range(4)
                ):
                    return True
    return False


def is_full(board):
    return all(board[0][column] != EMPTY for column in range(COLUMNS))


def play_game():
    board = create_board()
    player = 0
    print("Connect Four")
    print("Enter a column number, or q to quit.")

    while True:
        display_board(board)
        choice = input(f"Player {player + 1} ({TOKENS[player]}), choose a column: ").strip()
        if choice.lower() == "q":
            print("Game ended.")
            return
        if not choice.isdigit() or not drop_piece(board, int(choice) - 1, TOKENS[player]):
            print("Choose an available column from 1 to 7.")
            continue
        if has_won(board, TOKENS[player]):
            display_board(board)
            print(f"Player {player + 1} wins!")
            return
        if is_full(board):
            display_board(board)
            print("It's a draw!")
            return
        player = 1 - player


if __name__ == "__main__":
    play_game()