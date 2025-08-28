import random
import tkinter as tk
from tkinter import messagebox

print("hi! welcome to the guessing number game")

import random

attempts = 7
random_number = None
low = None
high = None

def start_game():
    global low, high, random_number, attempts
    try:
        low = int(low_entry.get())
        high = int(high_entry.get())
        if low >= high:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid integer bounds (low < high).")
        return

    random_number = random.randint(low, high)
    attempts = 7
    bounds_frame.pack_forget()
    game_frame.pack()
    prompt_label.config(text=f"Guess a number between {low} and {high}:")
    result_label.config(text=f"You have {attempts} attempts.")
    entry.delete(0, tk.END)
    entry.focus()

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
        return

    if guess == random_number:
        messagebox.showinfo("Congratulations!", f"You guessed the number {random_number} correctly!")
        root.destroy()
    else:
        attempts -= 1
        if attempts == 0:
            messagebox.showinfo("Game Over", f"Sorry, you've run out of attempts. The number was {random_number}.")
            root.destroy()
        else:
            hint = "higher" if guess < random_number else "lower"
            result_label.config(text=f"Try {hint}! Attempts left: {attempts}")
            entry.delete(0, tk.END)
            entry.focus()

root = tk.Tk()
root.title("Guess the Number Game")

# Frame for bounds input
bounds_frame = tk.Frame(root)
bounds_frame.pack(pady=10)

tk.Label(bounds_frame, text="Enter the lower bound:").grid(row=0, column=0, padx=5, pady=5)
low_entry = tk.Entry(bounds_frame)
low_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(bounds_frame, text="Enter the upper bound:").grid(row=1, column=0, padx=5, pady=5)
high_entry = tk.Entry(bounds_frame)
high_entry.grid(row=1, column=1, padx=5, pady=5)

start_button = tk.Button(bounds_frame, text="Start Game", command=start_game)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

# Frame for the guessing game
game_frame = tk.Frame(root)

prompt_label = tk.Label(game_frame, text="")
prompt_label.pack(pady=10)

entry = tk.Entry(game_frame)
entry.pack(pady=5)

guess_button = tk.Button(game_frame, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(game_frame, text="")
result_label.pack(pady=10)

root.mainloop()
# To export this file to your GitHub repository, you can use the GitHub web interface or Git command line.
# Example using Git (run these commands in your terminal):

# 1. Initialize git (if not already done)
#    git init

# 2. Add your file
#    git add "# Python Basics.py"

# 3. Commit your changes
#    git commit -m "Add guessing number game using tkinter"

# 4. Add your GitHub repository as a remote (replace URL with your repo)
#    git remote add origin https://github.com/yourusername/your-repo.git

# 5. Push to GitHub
#    git push -u origin main

# Alternatively, upload the file directly using the GitHub website.