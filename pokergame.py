import tkinter as tk
from tkinter import messagebox
import random

# These are the games rules for the user to understand how to play the game. 
RULES = """
Betting Options:
The player can bet on one of the following options:

Number: The player guesses a specific number between 1 and 10.
High: The player bets that the winning number will be greater than 5 (i.e., 6, 7, 8, 9, or 10).
Low: The player bets that the winning number will be 5 or less (i.e., 1, 2, 3, 4, or 5).
Odd: The player bets that the winning number will be an odd number (i.e., 1, 3, 5, 7, or 9).
Even: The player bets that the winning number will be an even number (i.e., 2, 4, 6, 8, or 10).

Placing Bets:
The player chooses a bet type from the options provided.
The player enters the amount they want to bet. The bet amount must be a positive number and cannot exceed the current balance.

Winning and Losing:
A winning number between 1 and 10 is randomly generated.
The outcome is determined based on the player's choice:
Number: If the player guessed the exact number, they win 10 times their bet amount.
High: If the winning number is greater than 5, the player wins an amount equal to their bet.
Low: If the winning number is 5 or less, the player wins an amount equal to their bet.
Odd: If the winning number is odd, the player wins an amount equal to their bet.
Even: If the winning number is even, the player wins an amount equal to their bet.
If the player's guess is incorrect, they lose the bet amount.

Continuing the Game:
After each round, the player can choose to continue playing or quit the game.
The game continues as long as the player has a positive balance and chooses to keep playing.
The game ends if the player's balance reaches zero or if the player decides to quit.

Ending the Game:
If the player chooses to quit the game or is out of balance then the player's final balance is displayed.
"""

def play_round(balance, bet, choice, player_number=None):
    winning_number = random.randint(1, 10)
    print(f"The winning number is {winning_number}.")
    result_message = ""
    winnings = 0

    if choice == 'number':
        if player_number == winning_number:
            winnings = bet * 10
            result_message = f"Congratulations! You won ${winnings}!"
            balance += winnings
        else:
            result_message = "Sorry, you lost."
            balance -= bet
            
    elif choice == 'high':
        if winning_number > 5:
            result_message = "Congratulations! You guessed 'high' correctly!"
            balance += bet
        else:
            result_message = "Sorry, you lost."
            balance -= bet
            
    elif choice == 'low':
        if winning_number <= 5:
            result_message = "Congratulations! You guessed 'low' correctly!"
            balance += bet
        else:
            result_message = "Sorry, you lost."
            balance -= bet
    elif choice == 'even':
        if winning_number % 2 == 0:
            result_message = "Congratulations! You guessed 'even' correctly!"
            balance += bet
        else:
            result_message = "Sorry, you lost."
            balance -= bet
    elif choice == 'odd':
        if winning_number % 2 != 0:
            result_message = "Congratulations! You guessed 'odd' correctly!"
            balance += bet
        else:
            result_message = "Sorry, you lost."
            balance -= bet

    return balance, result_message

# Main GUI application class
class PokerGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Poker Game")
        self.geometry("450x450")
        self.balance = 1000
        self.player_name = ""
        self.create_widgets()

    def create_widgets(self):
        self.current_screen = None
        self.show_rules_screen()

    def clear_screen(self):
        if self.current_screen:
            for widget in self.current_screen.winfo_children():
                widget.destroy()
            self.current_screen.pack_forget()
            self.current_screen = None

    def show_rules_screen(self):
        self.clear_screen()
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True)

        rules_label = tk.Label(self.current_screen, text=RULES, wraplength=400, justify="left")
        rules_label.pack(pady=20)

        agree_button = tk.Button(self.current_screen, text="I Agree", command=self.show_name_screen)
        agree_button.pack(pady=20)

    def show_name_screen(self):
        self.clear_screen()
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True)

        name_label = tk.Label(self.current_screen, text="Please enter your name:")
        name_label.pack(pady=10)

        self.name_entry = tk.Entry(self.current_screen)
        self.name_entry.pack(pady=10)

        next_button = tk.Button(self.current_screen, text="Next", command=self.save_name_and_show_bet_screen)
        next_button.pack(pady=10)

    def save_name_and_show_bet_screen(self):
        self.player_name = self.name_entry.get()
        if not self.player_name:
            messagebox.showerror("Error", "Name cannot be empty!")
            return
        self.show_bet_screen()

    def show_bet_screen(self):
        self.clear_screen()
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True)

        balance_label = tk.Label(self.current_screen, text=f"Your current balance is ${self.balance}")
        balance_label.pack(pady=10)

        bet_label = tk.Label(self.current_screen, text="Enter your bet:")
        bet_label.pack(pady=10)

        self.bet_entry = tk.Entry(self.current_screen)
        self.bet_entry.pack(pady=10)

        next_button = tk.Button(self.current_screen, text="Next", command=self.save_bet_and_show_choice_screen)
        next_button.pack(pady=10)

    def save_bet_and_show_choice_screen(self):
        try:
            self.bet = float(self.bet_entry.get())
            if self.bet <= 0:
                raise ValueError("Bet must be a positive number!")
            if self.bet > self.balance:
                raise ValueError("You cannot bet more than your current balance!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        self.show_choice_screen()

    def show_choice_screen(self):
        self.clear_screen()
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True)

        choice_label = tk.Label(self.current_screen, text="Choose your bet (number / high / low / even / odd):")
        choice_label.pack(pady=10)

        self.choice_entry = tk.Entry(self.current_screen)
        self.choice_entry.pack(pady=10)

        number_label = tk.Label(self.current_screen, text="If you chose 'number', enter your number (1-10):")
        number_label.pack(pady=10)

        self.number_entry = tk.Entry(self.current_screen)
        self.number_entry.pack(pady=10)

        play_button = tk.Button(self.current_screen, text="Play", command=self.play_game)
        play_button.pack(pady=10)

    def play_game(self):
        choice = self.choice_entry.get().lower()
        number = None
        if choice == 'number':
            try:
                number = int(self.number_entry.get())
                if not 1 <= number <= 10:
                    raise ValueError("Number must be between 1 and 10!")
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return

        self.balance, result_message = play_round(self.balance, self.bet, choice, number)
        self.show_result_screen(result_message)

    def show_result_screen(self, result_message):
        self.clear_screen()
        self.current_screen = tk.Frame(self)
        self.current_screen.pack(expand=True)

        result_label = tk.Label(self.current_screen, text=result_message)
        result_label.pack(pady=10)

        balance_label = tk.Label(self.current_screen, text=f"Your current balance is ${self.balance}")
        balance_label.pack(pady=10)

        if self.balance <= 0:
            messagebox.showinfo("Game Over", "You have run out of money. Game over.")
            self.quit()
        else:
            play_again_button = tk.Button(self.current_screen, text="Play Again", command=self.show_bet_screen)
            play_again_button.pack(pady=10)

            quit_button = tk.Button(self.current_screen, text="Quit", command=self.quit)
            quit_button.pack(pady=10)

if __name__ == "__main__":
    app = PokerGameApp()
    app.mainloop()
