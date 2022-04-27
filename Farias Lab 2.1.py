# IT 280 – Lab #2: Guessing Game (Rock, Paper, Scissors, Lizard, Spock)

import random

# Defining global variables
message = 'Hello. Press the key for playing (R)ock, (P)aper, (Sc)issors, (L)izard, (Sp)ock, or (q)uit? '
optionList = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


def printWinner(userOption, computerOption):
    # Rock logic
    if userOption == 'r' or computerOption == 'Rock':
        if userOption == 'r' and computerOption == 'Lizard':
            print('User Wins! Rock crushes Lizard')
            return
        elif userOption == 'r' and computerOption == 'Scissors':
            print('User Wins! Rock destroys Scissors')
            return
        elif computerOption == 'Rock' and userOption == 'l':
            print('Computer Wins! Rock crushes Lizard')
            return
        elif computerOption == 'Rock' and userOption == 'sc':
            print('Computer Wins! Rock destroys Scissors')
            return

    # Paper logic
    if userOption == 'p' or computerOption == 'Paper':
        if userOption == 'p' and computerOption == 'Spock':
            print('User Wins! Paper disproves Spock')
            return
        elif userOption == 'p' and computerOption == 'Rock':
            print('User Wins! Paper covers Rock')
            return
        elif computerOption == 'Paper' and userOption == 'sp':
            print('Computer Wins! Paper disproves Spock')
            return
        elif computerOption == 'Paper' and userOption == 'r':
            print('Computer Wins! Paper covers Rock')
            return

    # Scissors logic
    if userOption == 'sc' or computerOption == 'Scissors':
        if userOption == 'sc' and computerOption == 'Paper':
            print('User Wins! Scissors cuts Paper')
            return
        elif userOption == 'sc' and computerOption == 'Lizard':
            print('User Wins! Scissors decapitates Lizard')
            return
        elif computerOption == 'Scissors' and userOption == 'p':
            print('Computer Wins! Scissors cuts Paper')
            return
        elif computerOption == 'Scissors' and userOption == 'l':
            print('Computer Wins! Scissors decapitates Lizard')
            return

    # Lizard logic
    if userOption == 'l' or computerOption == 'Lizard':
        if userOption == 'l' and computerOption == 'Paper':
            print('User Wins! Lizard eats Paper')
            return
        elif userOption == 'l' and computerOption == 'Spock':
            print('User Wins! Lizard Poisons Spock')
            return
        elif computerOption == 'Lizard' and userOption == 'p':
            print('Computer Wins! Lizard eats Paper')
            return
        elif computerOption == 'Lizard' and userOption == 'sp':
            print('Computer Wins! Lizard Poisons Spock')
            return

    # Spock logic
    if userOption == 'sp' or computerOption == 'Spock':
        if userOption == 'sp' and computerOption == 'Scissors':
            print('User Wins! Spock smashes Scissors')
            return
        elif userOption == 'sp' and computerOption == 'Rock':
            print('User Wins! Spock vaporizes Rock')
            return
        elif computerOption == 'Spock' and userOption == 'sc':
            print('Computer Wins! Spock smashes Scissors')
            return
        elif computerOption == 'Spock' and userOption == 'r':
            print('Computer Wins! Spock vaporizes Rock')
            return

    # No winner
    print('Nobody wins! both choose the same. Try again.')


# Starting initial variables and values
userOption = input(message)
computerOption = random.choice(optionList)

# Looping for keeping playing
while userOption != 'q':
    printWinner(userOption, computerOption)
    print()
    userOption = input(message)
    computerOption = random.choice(optionList)

# Quit program
print('Thank you for playing. Bye!')
