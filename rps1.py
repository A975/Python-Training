import sys
import random
from enum import Enum

class RPS(Enum):

    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:

    # print(RPS(2)) //RPS.PAPER

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

    if player == 1 and computer == 3:
        print("🎉You win!")
    elif player == 2 and computer == 1:
        print("✨You win!")
    elif player == 3 and computer == 2:
        print("🎶You win!")
    elif player == computer:
        print("🌹Tie game!") 


    playagain = input("\nPlay again ? \n Y for Yes or \nQ to Quit \n\n")


    if playagain.lower() == "y":

        continue

    else:

        print("✨✨✨")
        print("Thank you for playing! \n")
        playagain = False

sys.exit("Bye! 🤞 wave")