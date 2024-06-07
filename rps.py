import sys
import random
from enum import Enum

class RPS(Enum):

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print(RPS(2)) //RPS.PAPER

value = input('Please enter a value: \n')
 
print(value)

print("\nPlay again?")

playerchoice = input("Enter...\n1 for Rock \n2 for Paper, or \n3 for Scissors: \n\n")

player = int(playerchoice)

if player < 1 | player > 3:

    sys.exit('You must enter 1,2 or 3.')

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You chose" + playerchoice + ".")
print("Python chose " + computerchoice + ".")
print("")

if player == 1:
    print("🎉You win!")
elif player == 2 and computer == 1:
    print("✨Python win!")
elif player == computer:
    print("🎶Tie game!")
else:
    print("🌹Python wins!")