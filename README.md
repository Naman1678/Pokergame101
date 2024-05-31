This is a beginner-friendly poker game designed for new users learning how to play poker. The game provides the user with $1000 for the initial play, and after that, it starts adding and removing money based on the winnings and losses of the user.

## Game Rules

### Betting Options:
The player can bet on one of the following options:

- **Number**: The player guesses a specific number between 1 and 10.
- **High**: The player bets that the winning number will be greater than 5 (i.e., 6, 7, 8, 9, or 10).
- **Low**: The player bets that the winning number will be 5 or less (i.e., 1, 2, 3, 4, or 5).
- **Odd**: The player bets that the winning number will be an odd number (i.e., 1, 3, 5, 7, or 9).
- **Even**: The player bets that the winning number will be an even number (i.e., 2, 4, 6, 8, or 10).

### Placing Bets:
- The player chooses a bet type from the options provided.
- The player enters the amount they want to bet. The bet amount must be a positive number and cannot exceed the current balance.

### Winning and Losing:
- A winning number between 1 and 10 is randomly generated.
- The outcome is determined based on the player's choice:
  - **Number**: If the player guessed the exact number, they win 10 times their bet amount.
  - **High**: If the winning number is greater than 5, the player wins an amount equal to their bet.
  - **Low**: If the winning number is 5 or less, the player wins an amount equal to their bet.
  - **Odd**: If the winning number is odd, the player wins an amount equal to their bet.
  - **Even**: If the winning number is even, the player wins an amount equal to their bet.
- If the player's guess is incorrect, they lose the bet amount.

### Continuing the Game:
- After each round, the player can choose to continue playing or quit the game.
- The game continues as long as the player has a positive balance and chooses to keep playing.
- The game ends if the player's balance reaches zero or if the player decides to quit.

### Ending the Game:
- If the player chooses to quit the game or is out of balance, then the player's final balance is displayed.

## How to Run the Game

1. **Install Python**: Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Clone the Repository**: Clone this repository to your local machine using:
    ```bash
    git clone <repository-url>
    ```

3. **Navigate to the Project Directory**:
    ```bash
    cd <project-directory>
    ```

4. **Run the Game**: Execute the game script using Python:
    ```bash
    python poker_game.py
    ```

## Game Flow

1. **Rules Screen**: The game starts by displaying the rules of the game and an "I Agree" button.
2. **Name Screen**: After clicking "I Agree", the player is asked to enter their name.
3. **Bet Screen**: The player then enters the amount they want to bet.
4. **Choice Screen**: The player chooses their bet type (number, high, low, even, odd) and the specific number if "number" is chosen.
5. **Result Screen**: The game displays the result and asks if the player wants to play another round or quit.
