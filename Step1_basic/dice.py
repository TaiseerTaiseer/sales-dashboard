import random

# Welcome message 
print("Welcome to the dice Game")

# Ask the user to roll the dice
input("Press Enter  to roll the dice...")

# Generate a random number between 1 and 6
dice_roll = random.randint(1, 6)

# show the result
print("You rolled a", dice_roll)

# win condition
if dice_roll == 6:
    print("You win")
else:
    print("Try agin!")