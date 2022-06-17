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
    # secret_number.append(randint(1, 9))
    
    # while True:
    #     random_number = randint(0, 9)
    #     if secret_number[0] != random_number:
    #         secret_number.append(random_number)
    #         break
            
    # while True:
    #     random_number = randint(0, 9)
    #     if secret_number[0] != random_number and secret_number[1] != random_number:
    #         secret_number.append(random_number)
    #         break
    secret_number = [1, 2, 3]
    return    

user_guess = 0
# ask the user for an guess 
def ask_guess(number_of_tries):
    global user_guess
    user_guess = input(f'guess #{number_of_tries}\n')

# check for fermi
def check_fermi():
    
    if secret_number[0] == int(user_guess[0]):

        return True
    elif secret_number[1] == int(user_guess[1]):
    
        return True
    elif secret_number[2] == int(user_guess[2]):
        
        return True
    else:
        return False
    
# check for piko 
def check_piko():
    for i in secret_number:
        for j in user_guess:
            if int(j) == i:
            
                return True

def check_win():
    global secret_number
    if secret_number[0] * 100 + secret_number[1] * 10 + secret_number[2] == int(user_guess):
        print('You got it!')
        return True
        
# give the hints to the user
# repet this proses unil the user guesses coretly and the game end or if the user guessed to many times
def start_new_game():
    print('''I am thinking of a 3-digit number. Try to guess what it is.
The clues I give are...
When I say: That means:
 Bagels None of the digits is correct.
 Pico One digit is correct but in the wrong position.
 Fermi One digit is correct and in the right position.''')
    
    make_secret_number()
    counter = 0
    print('I have thought up a number. You have 10 guesses to get it.')
    while True:
        
        counter += 1
        ask_guess(counter)
        if check_win():
            if input('Do you want to play again? (yes or no)\n') != 'yes':
                return
            else:
                make_secret_number()    
        elif counter > 10:
            print('you took to long to guess the number')
            if input('Do you want to play again? (yes or no)\n') != 'yes':
                return
            else:
                make_secret_number()
            
        else:     
            if check_fermi():
                print('firmi')
            if check_piko():
                print('piko')
            elif check_fermi() == False:    
                print('bagel')
        
# ask the user if they want to play again