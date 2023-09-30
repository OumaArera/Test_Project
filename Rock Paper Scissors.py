import random

# player choice
player = int(input("Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(f"Player choice is {player}")

# computer choice
computer = random.randint(0, 2)
print(f"Computer choice is {computer}")

# Scenario where Player wins
if player == 0 and computer == 2:
    print("Player wins!")

elif player == 1 and computer == 0:
    print("Player wins!")

elif player == 2 and computer == 1:
    print("Player wins!")

elif computer == 0 and player == 1:
    print("Player Wins!")

elif computer == 1 and player == 2:
    print("Player wins!")

elif computer == 2 and player == 0:
    print("Player wins!")

# Scenario where the Computer wins

elif computer == 0 and player == 2:
    print("Computer wins!")

elif computer == 1 and player == 0:
    print("Computer wins!")

elif computer == 2 and player == 1:
    print("Computer wins!")

elif player == 0 and computer == 1:
    print("Computer Wins!")

elif player == 1 and computer == 2:
    print("Computer wins!")

elif player == 2 and computer == 0:
    print("computer wins!")

# Scenario where there would be a draw

if player == 0 and computer == 0:
    print("Draw!")

elif player == 1 and computer == 1:
    print("Draw!")

elif player == 2 and computer == 2:
    print("Draw!")

