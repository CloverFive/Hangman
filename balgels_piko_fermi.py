# The Bagels Deduction Game
from random import randint

# Sample Output:

# I am thinking of a 3-digit number. Try to guess what it is.
# The clues I give are...
# When I say: That means:
#  Bagels None of the digits is correct.
#  Pico One digit is correct but in the wrong position.
#  Fermi One digit is correct and in the right position.
# I have thought up a number. You have 10 guesses to get it.
# Guess #1:
# 123
# Fermi
# Guess #2:
# 453
# Pico
# Guess #3:
# 425
# Fermi
# Guess #4:
# 326
# Bagels
# Guess #5:
# 489
# Bagels
# Guess #6:
# 075
# Fermi Fermi
# Guess #7:
# 015
# Fermi Pico
# Guess #8:
# 175
# You got it!
# Do you want to play again? (yes or no)
# no

secret_number = []
# generate a list of three random numbers 
def make_secret_number():

    global secret_number
    secret_number.append(randint(1, 9))
    
    while True:
        random_number = randint(0, 9)
        if secret_number[0] != random_number:
            secret_number.append(random_number)
            break
            
    while True:
        random_number = randint(0, 9)
        if secret_number[0] != random_number and secret_number[1] != random_number:
            secret_number.append(random_number)
            break
    return    

user_guess = 0
# ask the user for an guess 
def ask_guess(number_of_tries):
        global user_guess = int(input(f'guess #{number_of_tries}')

# check for fermi
def check_fermi():
    if secret_number[0] == user_guess[0]:
        print('fermi')
        return True
    elif secret_number[1] == user_guess[1]:
        print('fermi')
        return True
    elif sectet_number[2] == user_guess[2]:
        print('fermi')
        return True
    else:
        return False
    
# check for piko 
def check_piko():
    for i in secret_number:
        for j in user_guess:
            if j = i:
                print('piko')
                return True

# check for bagel
def check_bagel():
    if check_piko == False and check_firmi == False:
        print('bagel')
        return True
    else:
        return False

def check_win():
    if random_number[0] *  == 
        
# give the hints to the user
# repet this proses unil the user guesses coretly and the game end or if the user guessed to many times
def start_new_game():
    print('''I am thinking of a 3-digit number. Try to guess what it is.
The clues I give are...
When I say: That means:
 Bagels None of the digits is correct.
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.''')
    
    secret_number()
    print('I have thought up a number. You have 10 guesses to get it.')
    while True:
        
        ask_guess(i)
        check_fermi()
        check_piko()
        check_bagel()
    
    print('you took to long to guess the number')
        
# ask the user if they want to play again