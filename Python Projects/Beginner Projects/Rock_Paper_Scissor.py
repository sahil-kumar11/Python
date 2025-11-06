import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter a choice of Rock/Paper/Scissor and q for quit: ").lower()
    if user_input.lower() == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_picks = options[random_number]
    print("Computer Picks: ", computer_picks)

    if user_input == "rock" and computer_picks == "scissors":
        print("You win this round")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_picks == "rock":
        print("You win this round")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_picks == "paper":
        print("You win this round")
        user_wins += 1
        continue
    
    else:
        print("Computer wins this round")
        computer_wins += 1

print("you won: ",user_wins,"times.")
print("computer won: ",computer_wins,"times.")
print("GoodBye!")