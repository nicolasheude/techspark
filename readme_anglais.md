## The Matchstick Game: Master the Strategy!

**Objective:** Create a Python game where two players take turns removing matches from a pile. The player who removes the last match wins!

https://techsparkacademy.ch/python-basics-cheat-sheet/

**Game Rules:**

1. **The Matchstick Pile:** At the beginning of the game, there are a certain number of matches on the field (you can choose this number).
2. **The Players:** There are two players: player 1 and player 2.
3. **The Game Round:** Each player takes turns removing 1, 2, or 3 matches from the pile.
4. **End of Game:** The player who removes the last match wins the game!

**Your mission:**

Create a Python program that allows you to play the matchstick game. Here are the steps to follow:

1. **Function `get_player_names`:**
   - This function asks for the players' names.
   - It returns a list containing the names of the two players.

2. **Function `get_number_of_matches`:**
   - This function asks for the number of matches at the beginning of the game.
   - It returns the number of matches chosen by the players.

3. **Function `play_round`:**
   - This function allows to play a round of the game.
   - It takes as arguments the name of the current player, the number of matches left and a boolean indicating whether the AI is playing (True if the AI is playing, False otherwise).
   - If the AI is playing, it randomly chooses a number of matches to remove.
   - If the human player is playing, the function asks him how many matches he wants to remove.
   - The function checks if the player has entered a valid number (between 1 and 3).
   - The function removes the chosen number of matches from the pile and returns the new number of matches left.

4. **Function `check_game_end`:**
   - This function checks if the game is over.
   - It takes as argument the number of matches left.
   - If the number of matches is 0, the function returns True, indicating that the game is over. Otherwise, it returns False.

5. **Function `play_against_player`:**
   - This function allows two players to compete.
   - It takes as arguments the names of the two players and the number of matches at the beginning.
   - The function uses the `play_round` and `check_game_end` functions to manage the rounds of the game.
   - The function displays the name of the winner at the end of the game.

6. **Function `play_against_random_ai`:**
   - This function allows a player to play against a random AI.
   - It takes as arguments the name of the player and the number of matches at the beginning.
   - The function uses the `play_round` and `check_game_end` functions to manage the rounds of the game.
   - The AI randomly chooses a number of matches to remove between 1 and 3.
   - The function displays the name of the winner at the end of the game.

7. **Function `play_against_avoid_errors_ai`:**
   - This function allows a player to play against an AI that tries to avoid basic errors.
   - It takes as arguments the name of the player and the number of matches at the beginning.
   - The function uses the `play_round` and `check_game_end` functions to manage the rounds of the game.
   - The AI uses a simple strategy to try to force the player to make the last take. For example, if the number of matches is a multiple of 4, the AI can remove 1 match to leave the player facing a number of matches multiple of 4.
   - The function displays the name of the winner at the end of the game.

8. **Function `play_against_ultra_strong_ai`:**
   - This function allows a player to play against an AI that uses a winning strategy.
   - It takes as arguments the name of the player and the number of matches at the beginning.
   - The function uses the `play_round` and `check_game_end` functions to manage the rounds of the game.
   - The AI uses a strategy to force the player to make the last take, using an algorithm to choose the best possible moves.
   - The function displays the name of the winner at the end of the game.

9. **Create a main menu:**
   - Ask the player to choose a game mode:
     - Play against another player
     - Play against a random AI
     - Play against an AI that avoids basic errors
     - Play against an ultra-strong AI

10. **Launch the game according to the player's choice:**
    - Call the corresponding function depending on the player's choice.

**Basic Code:**

```python
import random

def get_player_names():
  """Asks for the players' names."""
  # ... (To be completed) ...

def get_number_of_matches():
  """Asks for the number of matches at the beginning of the game."""
  # ... (To be completed) ...

def play_round(current_player_name, matches_left, ia=False):
  """Allows to play a round of the game."""
  # ... (To be completed) ...

def check_game_end(matches_left):
  """Checks if the game is over."""
  # ... (To be completed) ...

def play_against_player(player1_name, player2_name, matches):
  """Allows two players to compete."""
  # ... (To be completed) ...

def play_against_random_ai(player_name, matches):
  """Allows a player to play against a random AI."""
  # ... (To be completed) ...

def play_against_avoid_errors_ai(player_name, matches):
  """Allows a player to play against an AI that avoids basic errors."""
  # ... (To be completed) ...

def play_against_ultra_strong_ai(player_name, matches):
  """Allows a player to play against an ultra-strong AI."""
  # ... (To be completed) ...

# Start of the game
while True:
  # ... (To be completed) ...
```

**Tips:**

- Use the `input()` functions to get player input.
- Use `while` loops to repeat the game rounds.
- Use `if` conditions to manage the different player actions.
- Use the `random.randint()` function to generate random numbers for the AI.
- Use variables to store the number of matches left and the players' names.

**Possible Enhancements:**

- You can add additional features, such as:
    - Displaying the players' score.
    - Asking players if they want to play again.
    - Creating a more attractive graphical interface.
    - Implementing more complex AIs.

**Good luck and have fun creating your matchstick game!**


## Deciphering the Error-Avoiding AI

The "error-avoiding" AI is a bit cunning. It tries to trick you into having to pick the last match!

Here's how it works:

1. **The Goal:** The AI tries to always leave you with a number of matches that is a **multiple of 4** (4, 8, 12, 16, etc.).

2. **The Strategy:**

   - **If the number of matches is already a multiple of 4:** The AI will remove a random number of matches (1, 2 or 3) to break this pattern.
   - **If the number of matches is not a multiple of 4:** The AI will remove the necessary number of matches to bring the total back to a multiple of 4.

3. **Example:**

   - Imagine there are 11 matches. This is not a multiple of 4.
   - The AI will remove 3 matches to leave 8 matches (8 is a multiple of 4).
   - Now it's your turn. No matter how many matches you remove (1, 2 or 3), the AI will always be able to make the remaining number a multiple of 4.
   - If you remove 2 matches, there are 6 matches left. The AI will remove 2 matches to leave 4 matches.
   - If you remove 3 matches, there are 5 matches left. The AI will remove 1 match to leave 4 matches.

4. **The Trap:**

   - If you fall into the trap and leave a multiple of 4, the AI will always be able to force you to take the last match!

**How to translate this logic into Python?**

You can use the modulo operator (%) to find the remainder of a division. For example, `11 % 4` gives 3, because 11 divided by 4 gives 2 with a remainder of 3.

- If the remainder of dividing the number of matches by 4 is 1, the AI should remove 1 match.
- If the remainder is 2, the AI should remove 2 matches.
- If the remainder is 3, the AI should remove 3 matches.
- If the remainder is 0, the AI can remove a random number of matches.

Don't forget to use the `random.randint(1, 3)` function to choose a random number between 1 and 3 if needed.

Feel free to ask if you have any questions! Good luck programming your AI! 

