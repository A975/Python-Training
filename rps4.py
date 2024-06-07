import sys
import random
from enum import Enum


def play_rps():

    class RPS(Enum):

        ROCK = 1
        PAPER = 2
        SCISSORS = 3
    
    # print(RPS(2)) //RPS.PAPER

    value = input('Please enter a value: \n')
    
    print(value)

    print("\nPlay again?")

    playerchoice = input("Enter...\n1 for Rock \n2 for Paper, or \n3 for Scissors: \n\n")

    if playerchoice not in ["1","2","3"]:
        print("You must enter 1,2, or 3.")
        return play_rps()   

    player = int(playerchoice)

    if player < 1 | player > 3:

        sys.exit('You must enter 1,2 or 3.')

    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("")
    print("You chose" + playerchoice + ".")
    print("Python chose " + computerchoice + ".")
    print("")

    def decide_winner(player, computer):

        if player == 1 and computer == 3:
            print("🎉You win!")
        elif player == 2 and computer == 1:
            print("✨You win!")
        elif player == 3 and computer == 2:
            print("🎶You win!")
        elif player == computer:
            print("🌹Tie game!") 
        else:
            print("🎇Python wins!")

        print("\n Play again ?")
    
    game_result = decide_winner(player, computer)

    print(game_result)

    global game_count
    game_count += 1

    print("\nGame count: " + str(game_count))

    print("\n Play Again")

    while True:

        playagain = input("\nY for Yes or \nQ to Quit\n")
        if playagain.lower() not in ["y","q"]:
            continue
        else:
            break
    
    # playagain = input("\n Play again ? \n Y for Yes or \nQ to Quit \n\n")


    if playagain.lower() == "y":

        return play_rps()

    else:

        print("✨✨✨")
        print("Thank you for playing! \n")
        # playagain = False
        sys.exit("Bye! 🤞 wave")


play_rps()