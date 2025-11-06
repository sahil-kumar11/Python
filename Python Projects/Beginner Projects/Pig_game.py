'''Dice Game — A Simple Python Turn-Based Game for 2 to 4 Players

This is a command-line dice game where 2 to 4 players compete to reach a score of 50. Each player rolls a 
dice and accumulates points unless they roll a 1, which ends their turn and resets their round score to 0.

* Supports **2 to 4 players
* Each turn continues until the player decides to stop or rolls a 1
* First player to reach **50 points wins

1. Run the script in any Python interpreter.
2. Enter number of players (2–4).
3. On your turn, type `y` to roll the dice.
4. If you roll 1, your turn ends and you score 0 for that round.
5. Otherwise, keep rolling to increase your score — but risk rolling a 1!
6. First to reach 50 wins! 🎉

Enjoy the game and feel free to improve it further!'''


import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)