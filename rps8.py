import sys
import random
from enum import Enum

def rps(name='PlayerOne'):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):

            ROCK = 1
            PAPER = 2
            SCISSORS = 3
        
        # print(RPS(2)) //RPS.PAPER

        playerchoice = input( 

            f"\n{name}, please enter... \n1 for Rock, \n2 for Paper, or \n3 for Scissors: \n\n"
        
        )

        if playerchoice not in ["1","2","3"]:

            print("You must enter 1,2, or 3.")
            return play_rps()   

        player = int(playerchoice)
        
        if player < 1 | player > 3:

            sys.exit('You must enter 1,2 or 3.')

        computerchoice = random.choice("123")
         
        computer = int(computerchoice)

        print(f"\n You chose {str(RPS(player)).replace('RPS.','').title()}.")
        print(
            f"Python chose {str(RPS(computer)).replace('RPS.','').title()}.\n"
        )
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

            print("\n Play again {name} ?")
        
        game_result = decide_winner(player, computer)
        
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")

        print(f"\n Player wins: {str(player_wins)}")
              
        print(f"\n Python wins: {str(python_wins)}")
              
        print("\nPlay again ?")

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
    
    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(

        "-n","--name", metavar="name",
        required=True, help="The name of the person playing the game."
    
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()