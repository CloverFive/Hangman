from random import randint
# A fun game that plays like this: 
# H A N G M A N
#  +---+
#  |
#  |
#  |
#  ===
# Missed letters:
# ___
# Guess a letter.

hangman_pics = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']


def make_random_word():
    words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
 coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
 lion lizard llama mole monkey moose mouse mule newt otter owl panda
 parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
 skunk sloth snake spider stork swan tiger toad trout turkey turtle
 weasel whale wolf wombat zebra'''.split()

    random_number = randint(1, len(words))

    return words[random_number]

# make a function that asks for a lettter 
def ask_guess():
    guess = input("Guess a Letter\n")
    check_guess(guess)

# make a function that checks if it's right that will also out put a boolen for wether the  inputed letter is cprret or not
def check_guess(letter):

    if letter in random_word and letter not in correct_guesses:
        correct_guesses.append(letter)

    elif letter in correct_guesses:
        
        print('You have already guessed that letter. Choose again.')
        ask_guess()
        
    
    else:
        incorrect_guesses.append(letter)

# make a function that will update to a the hangman picture
# def update_hangman_v1():
    
#     print('Missed letters:', end= ' ')
#     for i in range(len(incorrect_guesses)):
#         print(incorrect_guesses[i], end= '')
#     print('\n')

#     if len(correct_guesses) >= 1:
#         for i in range(len(random_word)):
#             print(i)
#             for j in range(len(correct_guesses)):
            
#                 if random_word[i] == correct_guesses[j]:
#                     print(correct_guesses[j], end= '')
#                 else:
#                     print('_', end= '')
#     else:
#         for i in range(len(random_word)):
#             print('_', end= '')
#         print('\n')

def update_hangman_v2():

    print('Missed letters:', end= ' ')
    for i in range(len(incorrect_guesses)):
        print(incorrect_guesses[i], end= ', ')
    print('\n')
    
    for i in range(len(random_word)):
        if random_word[i] in correct_guesses:
            print(random_word[i], end= '')
        else:
            print('_', end= '')
    print('\n')

def check_complete():
    for i in random_word:
        if i not in correct_guesses:
            return False
        
    return True

def display_hangman():
    print(hangman_pics[len(incorrect_guesses)])

def start_new_game():
    global random_word
    global correct_guesses
    global incorrect_guesses
    
    random_word = make_random_word()
    correct_guesses = []
    incorrect_guesses = []
    print('H A N G M A N')

def play_hangman():
    # make an infinint while loop
    start_new_game()
    
    while True:
        display_hangman()
        update_hangman_v2()
        ask_guess() 
    
        if check_complete():
            
            print(f'Yes! The secret word is \"{random_word}\"! You have won!')
            if input('Do you want to play again? (yes or no)\n') != 'yes':
                   
                break
            else:
                start_new_game()
                
        if len(incorrect_guesses) == len(hangman_pics) - 1:
            
            display_hangman()
            print('you failed boo you! I am not telling you the secret word! Haha')
            if input('Do you want to play again? (yes or no)\n') != 'yes':
                   
                break
            else:
                start_new_game()