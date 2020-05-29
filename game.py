# game.py

import random

def check_choice(choice):
    if choice.upper() not in ["ROCK","PAPER","SCISSORS"]:
        print("\nYou entered an invalid input - SHAME ON YOU")
        quit()
    
def prompt_choice():
    return input('Please enter your choice: Rock, Paper or Scissors: ')

if __name__ == "__main__":
    
    print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print("\n  Rock, Paper, Scissors, Shoot! - THE GAME v1.0\n")
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    input('Press enter to continue\n')

#---------USER MOVES------------------

    user_choice = prompt_choice()

    check_choice(user_choice)

    print('\nYou have chosen ', user_choice.upper(),'\n')

#-------------AI MOVES--------------

    ai_choice = random.choice(["ROCK",'PAPER','SCISSORS'])

    print('The AI has chosen ', ai_choice)

#-----------RESULTS-----------------

