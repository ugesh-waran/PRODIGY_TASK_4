import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x350")
root.resizable(False, False)

current_player = "X"
board = [""] * 9

# Function to check for win
def check_winner():
    wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)]           # diagonals
    for a, b, c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Handle button click
def on_click(index):
    global current_player
    if board[index] == "" and not check_winner():
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
            disable_all()
        else:
            current_player = "O" if current_player == "X" else "X"

# Disable all buttons
def disable_all():
    for btn in buttons:
        btn.config(state="disabled")

# Reset the game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", state="normal")

# Create buttons
buttons = []
frame = tk.Frame(root)
frame.pack(pady=20)
for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
