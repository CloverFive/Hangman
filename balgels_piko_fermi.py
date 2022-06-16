# The Bagels Deduction Game

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

# generate a list of three random numbers 
def make_list():
    
# ask the user for an guess 
# comare the guess to the random numbers 
# check for fermi
# check for piko 
# check for bagel
# give the hints to the user
# repet this proses unil the user guesses coretly and the game end or if the user guessed to many times
# ask the user if they want to play again