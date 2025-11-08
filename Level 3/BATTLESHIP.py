import tkinter as tk
from tkinter import messagebox
import random

class BattleshipGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        
        self.grid_size = 10
        self.ship_sizes = [5, 4, 3, 3, 2]
        self.player1_board = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.player2_board = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.player1_shots = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.player2_shots = [[0] * self.grid_size for _ in range(self.grid_size)]
        
        self.game_mode = None
        self.setup_phase = True
        self.current_ship_index = 0
        self.orientation = "H"
        self.current_player = 1
        
        self.show_mode_selection()
        
    def show_mode_selection(self):
        mode_frame = tk.Frame(self.root)
        mode_frame.grid(row=0, column=0, padx=50, pady=50)
        
        tk.Label(mode_frame, text="Select Game Mode", font=("Arial", 20, "bold")).pack(pady=20)
        
        tk.Button(mode_frame, text="Player vs Computer", font=("Arial", 14),
                 command=lambda: self.start_game("PvC"), width=20, height=2).pack(pady=10)
        
        tk.Button(mode_frame, text="Player vs Player", font=("Arial", 14),
                 command=lambda: self.start_game("PvP"), width=20, height=2).pack(pady=10)
    
    def start_game(self, mode):
        self.game_mode = mode
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()
        if mode == "PvC":
            self.place_computer_ships()
        
    def create_widgets(self):
        title = tk.Label(self.root, text="Battleship", font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, columnspan=10, pady=10)
        
        instruction_text = f"Player 1: Place ship (size {self.ship_sizes[0]}). Click to place. Press 'R' to rotate." if self.game_mode == "PvP" else f"Place ship (size {self.ship_sizes[0]}). Click to place. Press 'R' to rotate."
        self.info_label = tk.Label(self.root, text=instruction_text, font=("Arial", 12))
        self.info_label.grid(row=1, column=0, columnspan=10, pady=5)
        
        player1_label = tk.Label(self.root, text="Player 1" if self.game_mode == "PvP" else "Your Board", 
                                font=("Arial", 14, "bold"), fg="blue")
        player1_label.grid(row=2, column=0, columnspan=10)
        
        self.player_buttons = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                btn = tk.Button(self.root, width=3, height=1, bg="lightblue",
                               command=lambda x=i, y=j: self.player_click(x, y))
                btn.grid(row=i+3, column=j, padx=1, pady=1)
                row.append(btn)
            self.player_buttons.append(row)
        
        self.rotate_btn = tk.Button(self.root, text="Rotate (R)", command=self.rotate_ship)
        self.rotate_btn.grid(row=13, column=0, columnspan=5, pady=10)
        
        player2_label = tk.Label(self.root, text="Player 2" if self.game_mode == "PvP" else "Computer Board", 
                                font=("Arial", 14, "bold"), fg="green")
        player2_label.grid(row=2, column=11, columnspan=10)
        
        self.computer_buttons = []
        for i in range(self.grid_size):
            row = []
            for j in range(self.grid_size):
                btn = tk.Button(self.root, width=3, height=1, bg="lightgreen", state="disabled",
                               command=lambda x=i, y=j: self.computer_click(x, y))
                btn.grid(row=i+3, column=j+11, padx=1, pady=1)
                row.append(btn)
            self.computer_buttons.append(row)
        
        self.root.bind('r', lambda e: self.rotate_ship())
        self.root.bind('R', lambda e: self.rotate_ship())
        
    def rotate_ship(self):
        if self.setup_phase:
            self.orientation = "V" if self.orientation == "H" else "H"
            orientation_text = 'Horizontal' if self.orientation == 'H' else 'Vertical'
            player_text = f"Player {self.current_player}: " if self.game_mode == "PvP" and self.current_player == 2 else ""
            self.info_label.config(text=f"{player_text}Place ship (size {self.ship_sizes[self.current_ship_index]}). Orientation: {orientation_text}")
    
    def player_click(self, x, y):
        if self.setup_phase:
            current_board = self.player1_board if self.current_player == 1 else self.player2_board
            if self.place_ship(current_board, x, y, self.ship_sizes[self.current_ship_index], self.orientation):
                self.update_player_display()
                self.current_ship_index += 1
                
                if self.current_ship_index >= len(self.ship_sizes):
                    if self.game_mode == "PvP" and self.current_player == 1:
                        self.current_player = 2
                        self.current_ship_index = 0
                        self.clear_player_board()
                        self.info_label.config(text=f"Player 2: Place ship (size {self.ship_sizes[0]}). Press 'R' to rotate.")
                    else:
                        self.setup_phase = False
                        self.current_player = 1
                        self.clear_both_boards()
                        self.info_label.config(text="Player 1's turn! Click on the right board to attack!")
                        self.enable_computer_board()
                else:
                    player_text = f"Player {self.current_player}: " if self.game_mode == "PvP" and self.current_player == 2 else ""
                    self.info_label.config(text=f"{player_text}Place ship (size {self.ship_sizes[self.current_ship_index]}). Press 'R' to rotate.")
        elif self.game_mode == "PvP" and self.current_player == 2:
            # Player 2 attacks Player 1's board (left board)
            if self.player2_shots[x][y] != 0:
                return
            
            if self.player1_board[x][y] > 0:
                self.player_buttons[x][y].config(bg="red", text="X")
                self.player2_shots[x][y] = 1
                self.info_label.config(text="Player 2 HIT!")
            else:
                self.player_buttons[x][y].config(bg="white", text="O")
                self.player2_shots[x][y] = -1
                self.info_label.config(text="Player 2 Miss!")
            
            if self.check_win(self.player1_board, self.player2_shots):
                messagebox.showinfo("Game Over", "Player 2 WINS!")
                self.root.quit()
            else:
                self.current_player = 1
                self.root.after(500, lambda: self.info_label.config(text="Player 1's turn!"))
    
    def clear_player_board(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.player_buttons[i][j].config(bg="lightblue", text="")
    
    def clear_both_boards(self):
        # Clear left board (show only hits/misses, not ships)
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.player_buttons[i][j].config(bg="lightblue", text="")
        
        # Clear right board
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.computer_buttons[i][j].config(bg="lightgreen", text="")
    
    def place_ship(self, board, x, y, size, orientation):
        positions = []
        
        if orientation == "H":
            if y + size > self.grid_size:
                return False
            for i in range(size):
                if board[x][y + i] != 0:
                    return False
                positions.append((x, y + i))
        else:
            if x + size > self.grid_size:
                return False
            for i in range(size):
                if board[x + i][y] != 0:
                    return False
                positions.append((x + i, y))
        
        for px, py in positions:
            board[px][py] = size
        
        return True
    
    def place_computer_ships(self):
        for size in self.ship_sizes:
            placed = False
            while not placed:
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - 1)
                orientation = random.choice(["H", "V"])
                placed = self.place_ship(self.player2_board, x, y, size, orientation)
    
    def update_player_display(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.current_player == 1:
                    if self.player1_board[i][j] > 0:
                        self.player_buttons[i][j].config(bg="darkblue")
                else:
                    if self.player2_board[i][j] > 0:
                        self.player_buttons[i][j].config(bg="darkblue")
    
    def enable_computer_board(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.computer_buttons[i][j].config(state="normal", bg="lightgreen")
    
    def computer_click(self, x, y):
        # Player 1 attacks Player 2's board (right board)
        if self.current_player != 1:
            return
        
        if self.player1_shots[x][y] != 0:
            return
        
        if self.player2_board[x][y] > 0:
            self.computer_buttons[x][y].config(bg="red", text="X", state="disabled")
            self.player1_shots[x][y] = 1
            player_text = "Player 1 " if self.game_mode == "PvP" else ""
            self.info_label.config(text=f"{player_text}HIT!")
        else:
            self.computer_buttons[x][y].config(bg="white", text="O", state="disabled")
            self.player1_shots[x][y] = -1
            player_text = "Player 1 " if self.game_mode == "PvP" else ""
            self.info_label.config(text=f"{player_text}Miss!")
        
        if self.check_win(self.player2_board, self.player1_shots):
            winner = "Player 1" if self.game_mode == "PvP" else "You"
            messagebox.showinfo("Game Over", f"{winner} WIN!")
            self.root.quit()
        else:
            if self.game_mode == "PvC":
                self.root.after(500, self.computer_turn)
            else:
                self.current_player = 2
                self.root.after(500, lambda: self.info_label.config(text="Player 2's turn! Click on the left board to attack!"))
    
    def computer_turn(self):
        x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
        while self.player_buttons[x][y].cget("text") in ["X", "O"]:
            x, y = random.randint(0, self.grid_size - 1), random.randint(0, self.grid_size - 1)
        
        if self.player1_board[x][y] > 0:
            self.player_buttons[x][y].config(bg="red", text="X")
            self.info_label.config(text="Computer HIT your ship!")
        else:
            self.player_buttons[x][y].config(bg="white", text="O")
            self.info_label.config(text="Computer missed. Your turn!")
        
        if self.check_win(self.player1_board, self.get_computer_shots()):
            messagebox.showinfo("Game Over", "Computer WINS!")
            self.root.quit()
    
    def get_computer_shots(self):
        shots = [[0] * self.grid_size for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.player_buttons[i][j].cget("text") == "X":
                    shots[i][j] = 1
        return shots
    
    def check_win(self, board, shots):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if board[i][j] > 0 and shots[i][j] != 1:
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipGUI(root)
    root.mainloop()