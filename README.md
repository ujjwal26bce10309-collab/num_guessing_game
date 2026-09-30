# 🎯 Number Guessing Game (Python)

A simple, interactive command-line game built with Python where the computer picks a random secret number, and the player tries to guess it with helpful hints along the way.


## 👨‍💻 Developer

**Developed by:** **Ujjwal Kumar**

## 📖 About the Game

The game is designed to be intuitive and beginner-friendly:
1. The computer selects a random integer between **1 and 100**.
2. The player is prompted to submit a guess via the terminal.
3. The computer evaluates the guess and gives immediate feedback:
   - 📉 **"Too low! Try again."** — if your guess is smaller than the secret number.
   - 📈 **"Too high! Try again."** — if your guess is greater than the secret number.
   - 🎉 **"Congratulations!"** — when you correctly identify the target number.
4. The program tracks the total number of attempts taken to reach the answer.

## 🧠 Core Programming Concepts Used

Here is an explanation of the underlying programming logic:
 1. Random Number Generation (`random.randint`)
Computers are deterministic by default, meaning they follow exact rules. Python's built-in `random` module provides functions to introduce unpredictability. `random.randint(1, 100)` picks an unpredictable integer within the inclusive range $[1, 100]$.
 2. Repetition & Loops (`while True`)
Instead of rewriting code for every guess, a **`while` loop** repeats a block of instructions continuously until a termination condition is met. The `break` statement exits the loop once the correct number is guessed.
3. User Input & Type Conversion (`input()` and `int()`)
When text is entered in the terminal, Python receives it as plain text (a `string`). Because mathematical comparisons (like greater-than or less-than) require numeric data, `int(...)` converts the text into a whole number (an integer).
 4. Conditional Logic (`if` / `elif` / `else`)
Branching logic decides what message to display:
- **`if`**: Checks if the guess is below the target.
- **`elif`** (short for *else if*): Checks if the guess is above the target.
- **`else`**: Executes when the guess is neither lower nor higher, meaning it is an exact match.

5. Error Handling (`try` / `except`)
If a player accidentally types a word (e.g., `"five"`) instead of numeric digits (`5`), the conversion would normally cause the program to crash. The `try-except` block intercepts the error gracefully and displays a friendly reminder without quitting the game.
🚀 How to Run the Game

-- Prerequisites
- Python 3.x installed on your computer.

-- Steps
1. **Clone or download** this repository.
2. Save the game script as `guess_game.py`.
3. Open your terminal or command prompt in the directory containing the file.
4. Run the script:
   python guess_game.py
5. Follow the on-screen instructions to play.
----THANKYOU FOR READING----
