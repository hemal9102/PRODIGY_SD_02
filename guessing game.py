import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.random_number = random.randint(1, 50)
        self.attempts = 0

        # Game Instructions
        self.instructions = tk.Label(root, text="Guess a number between 1 and 50", font=("Arial", 14))
        self.instructions.pack(pady=20)

        # Entry for User Guess
        self.guess_entry = tk.Entry(root, font=("Arial", 14))
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", self.check_guess)  # Bind Enter key to submit the guess

        # Feedback Label
        self.feedback_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.feedback_label.pack(pady=10)

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset Game", font=("Arial", 12), command=self.reset_game)
        self.reset_button.pack(pady=10)

    def check_guess(self, event=None):  # Accept the event parameter for key binding
        try:
            user_guess = int(self.guess_entry.get())
            self.attempts += 1

            if user_guess < self.random_number:
                self.feedback_label.config(text="Too Low! Try again.")
            elif user_guess > self.random_number:
                self.feedback_label.config(text="Too High! Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed it in {self.attempts} attempts!")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Enter valid integer")

    def reset_game(self):
        self.random_number = random.randint(1, 50)
        self.attempts = 0
        self.feedback_label.config(text="")
        self.guess_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
