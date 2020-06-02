# game.py

from os import system
import random

def check_choice(choice):
    if choice.upper() not in ["ROCK","PAPER","SCISSORS"]:
        print("\nYou entered an invalid input - SHAME ON YOU!!")
        quit()
    
def prompt_choice():
    return input('Please enter your choice: Rock, Paper or Scissors: ')


def who_won(player, player2):
    if player[1] == player2[1]:
        return "NO ONE!!"
    elif player[1] == "ROCK" and player2[1] == "SCISSORS":
        return player[0]
    elif player[1] == "PAPER" and player2[1] == "ROCK":
        return player[0]
    elif player[1] == "SCISSORS" and player2[1] == "PAPER":
        return player[0]
    else:
        return player2[0]

def end_message(winner):
    if winner == "You":
        print("\nWOOOOHOOOOO!!!! Winner winner chicken dinner!!! Please play again!\n")
        pass
    elif winner == "NO ONE!!":
        print("\nA Draw! That is a flaw! Please play again to redraw!\n")
        pass
    else:
        print("\nBoo! Improve your skill - Please play again!\n")
        pass

if __name__ == "__main__":
    
    system('clear')
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print("\n  Rock, Paper, Scissors, Shoot! - THE GAME v1.0\n")
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    input('Press enter to continue\n')

#---------USER MOVES------------------

    user_choice = prompt_choice()

    check_choice(user_choice)

    print('\nYou have chosen:', user_choice.upper(),'\n')

#-------------AI MOVES--------------

    ai_choice = random.choice(["ROCK",'PAPER','SCISSORS'])

    print('The AI has chosen:', ai_choice)

#-----------RESULTS-----------------
    Player = ['You',user_choice.upper()]
    Computer = ['AI', ai_choice.upper()]

    winner = who_won(Player, Computer)

    print('\n*********************************')
    print('\nWinner is ', winner, '\n')
    print('*********************************')

    end_message(winner)

#--------------END OF PROGRAM-----------------