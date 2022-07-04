from random import randint
from random import choice 
from random import shuffle
from math import sqrt
# Example Gameplay for Sonar

# S O N A R !
# TODO: Replace with instructions
#             1         2         3         4         5         
#    012345678901234567890123456789012345678901234567890123456789
#  0 ~`~``~``~``~`~`~```~`~``````~```~`~~~`~~```~~`~~~~~`~~`~~~~` 0
#  1 ~~~~~`~~~~~````~``~~```~``~`~`~`~``~~```~~~`~`~```~~~~`~`~~` 1
#  2 ```~````~``~`~`~~~``~~`````~~``~``~``~~```~~``~~`~~~````~~`~ 2
#  3 `````~~``````~`~~~~~```~~``~~~`~`~~~~~~`````~`~```~~~``~``~` 3
#  4 ~~~`~~~`~`~~~``~~~`~`~``~~~~``~~~~``~~~~`~`~``~~```~``~~`~`~ 4
#  5 `~``~````~`~`~~``~~~~``````~```~~~~````````~``~~~`~~``~~```` 5
#  6 ~`~```~~`~~```~````````~~```~```~~~~``~~~`~`~~`~``~~~`~~`~`` 6
#  7 ~`~~~```~``~```~`~```~~~~~~~`~~`~`~~~~``~```~~~`~```~``~``~` 7
#  8 `~``~~`~`~~`~~`~~``~```~````~`~```~``~````~~~````~~``~~``~~` 8
#  9 ~`~``~~````~~```~`~~```~~`~``~`~~``~`~`~~~~`~`~~`~`~```~~``` 9
# 10 `~~~~~~`~``~``~~~``~``~~~~`~``~```~`~~``~~~~~~``````~~`~``~~ 10
# 11 ~``~~~````~`~~`~~~`~~~``~``````~`~``~~~~`````~~~``````~`~`~~ 11
# 12 ~~~~~``~`~````~```~`~`~`~~`~~`~``~~~~~~~`~~```~~``~~`~~~~``` 12
# 13 `~~```~~````````~~~`~~~```~~~~~~~~`~~``~~`~```~`~~````~~~``~ 13
# 14 ```~``~`~`~``~```~`~``~`~``~~```~`~~~``~~``~```~`~~`~``````~ 14
#    012345678901234567890123456789012345678901234567890123456789
#              1         2         3         4         5         
# You have 20 sonar device(s) left. 3 treasure chest(s) remaining.
# Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
# 25 5
#              1         2         3         4         5
#    012345678901234567890123456789012345678901234567890123456789
#  0 ~`~``~``~``~`~`~```~`~``````~```~`~~~`~~```~~`~~~~~`~~`~~~~` 0
#  1 ~~~~~`~~~~~````~``~~```~``~`~`~`~``~~```~~~`~`~```~~~~`~`~~` 1
#  2 ```~````~``~`~`~~~``~~`````~~``~``~``~~```~~``~~`~~~````~~`~ 2
#  3 `````~~``````~`~~~~~```~~``~~~`~`~~~~~~`````~`~```~~~``~``~` 3
#  4 ~~~`~~~`~`~~~``~~~`~`~``~~~~``~~~~``~~~~`~`~``~~```~``~~`~`~ 4
#  5 `~``~````~`~`~~``~~~~````5`~```~~~~````````~``~~~`~~``~~```` 5
#  6 ~`~```~~`~~```~````````~~```~```~~~~``~~~`~`~~`~``~~~`~~`~`` 6
#  7 ~`~~~```~``~```~`~```~~~~~~~`~~`~`~~~~``~```~~~`~```~``~``~` 7
#  8 `~``~~`~`~~`~~`~~``~```~````~`~```~``~````~~~````~~``~~``~~` 8
#  9 ~`~``~~````~~```~`~~```~~`~``~`~~``~`~`~~~~`~`~~`~`~```~~``` 9
# 10 `~~~~~~`~``~``~~~``~``~~~~`~``~```~`~~``~~~~~~``````~~`~``~~ 10
# 11 ~``~~~````~`~~`~~~`~~~``~``````~`~``~~~~`````~~~``````~`~`~~ 11
# 12 ~~~~~``~`~````~```~`~`~`~~`~~`~``~~~~~~~`~~```~~``~~`~~~~``` 12
# 13 `~~```~~````````~~~`~~~```~~~~~~~~`~~``~~`~```~`~~````~~~``~ 13
# 14 ```~``~`~`~``~```~`~``~`~``~~```~`~~~``~~``~```~`~~`~``````~ 14
#   012345678901234567890123456789012345678901234567890123456789
#             1         2         3         4         5
# Treasure detected at a distance of 5 from the sonar device.
# You have 19 sonar device(s) left. 3 treasure chest(s) remaining.
# Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
# 30 5
#             1         2         3         4         5
#   012345678901234567890123456789012345678901234567890123456789
#  0 ~`~``~``~``~`~`~```~`~``````~```~`~~~`~~```~~`~~~~~`~~`~~~~` 0
#  1 ~~~~~`~~~~~````~``~~```~``~`~`~`~``~~```~~~`~`~```~~~~`~`~~` 1
#  2 ```~````~``~`~`~~~``~~`````~~``~``~``~~```~~``~~`~~~````~~`~ 2
#  3 `````~~``````~`~~~~~```~~``~~~`~`~~~~~~`````~`~```~~~``~``~` 3
#  4 ~~~`~~~`~`~~~``~~~`~`~``~~~~``~~~~``~~~~`~`~``~~```~``~~`~`~ 4
#  5 `~``~````~`~`~~``~~~~````5`~``3~~~~````````~``~~~`~~``~~```` 5
#  6 ~`~```~~`~~```~````````~~```~```~~~~``~~~`~`~~`~``~~~`~~`~`` 6
#  7 ~`~~~```~``~```~`~```~~~~~~~`~~`~`~~~~``~```~~~`~```~``~``~` 7
#  8 `~``~~`~`~~`~~`~~``~```~````~`~```~``~````~~~````~~``~~``~~` 8
#  9 ~`~``~~````~~```~`~~```~~`~``~`~~``~`~`~~~~`~`~~`~`~```~~``` 9
# 10 `~~~~~~`~``~``~~~``~``~~~~`~``~```~`~~``~~~~~~``````~~`~``~~ 10
# 11 ~``~~~````~`~~`~~~`~~~``~``````~`~``~~~~`````~~~``````~`~`~~ 11
# 12 ~~~~~``~`~````~```~`~`~`~~`~~`~``~~~~~~~`~~```~~``~~`~~~~``` 12
# 13 `~~```~~````````~~~`~~~```~~~~~~~~`~~``~~`~```~`~~````~~~``~ 13
# 14 ```~``~`~`~``~```~`~``~`~``~~```~`~~~``~~``~```~`~~`~``````~ 14
#   012345678901234567890123456789012345678901234567890123456789
#             1         2         3         4         5
# Treasure detected at a distance of 3 from the sonar device.
# You have 18 sonar device(s) left. 3 treasure chest(s) remaining.
# Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
# 25 10
#              1         2         3         4         5
#    012345678901234567890123456789012345678901234567890123456789
#  0 ~`~``~``~``~`~`~```~`~``````~```~`~~~`~~```~~`~~~~~`~~`~~~~` 0
#  1 ~~~~~`~~~~~````~``~~```~``~`~`~`~``~~```~~~`~`~```~~~~`~`~~` 1
#  2 ```~````~``~`~`~~~``~~`````~~``~``~``~~```~~``~~`~~~````~~`~ 2
#  3 `````~~``````~`~~~~~```~~``~~~`~`~~~~~~`````~`~```~~~``~``~` 3
#  4 ~~~`~~~`~`~~~``~~~`~`~``~~~~``~~~~``~~~~`~`~``~~```~``~~`~`~ 4
#  5 `~``~````~`~`~~``~~~~````5`~``3~~~~````````~``~~~`~~``~~```` 5
#  6 ~`~```~~`~~```~````````~~```~```~~~~``~~~`~`~~`~``~~~`~~`~`` 6
#  7 ~`~~~```~``~```~`~```~~~~~~~`~~`~`~~~~``~```~~~`~```~``~``~` 7
#  8 `~``~~`~`~~`~~`~~``~```~````~`~```~``~````~~~````~~``~~``~~` 8
#  9 ~`~``~~````~~```~`~~```~~`~``~`~~``~`~`~~~~`~`~~`~`~```~~``` 9
# 10 `~~~~~~`~``~``~~~``~``~~~4`~``~```~`~~``~~~~~~``````~~`~``~~ 10
# 11 ~``~~~````~`~~`~~~`~~~``~``````~`~``~~~~`````~~~``````~`~`~~ 11
# 12 ~~~~~``~`~````~```~`~`~`~~`~~`~``~~~~~~~`~~```~~``~~`~~~~``` 12
# 13 `~~```~~````````~~~`~~~```~~~~~~~~`~~``~~`~```~`~~````~~~``~ 13
# 14 ```~``~`~`~``~```~`~``~`~``~~```~`~~~``~~``~```~`~~`~``````~ 14
#    012345678901234567890123456789012345678901234567890123456789
#              1         2         3         4         5
# Treasure detected at a distance of 4 from the sonar device.
# You have 17 sonar device(s) left. 3 treasure chest(s) remaining.
# Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
# 29 8
#              1         2         3         4         5
#    012345678901234567890123456789012345678901234567890123456789
#  0 ~`~``~``~``~`~`~```~`~``````~```~`~~~`~~```~~`~~~~~`~~`~~~~` 0
#  1 ~~~~~`~~~~~````~``~~```~``~`~`~`~``~~```~~~`~`~```~~~~`~`~~` 1
#  2 ```~````~``~`~`~~~``~~`````~~``~``~``~~```~~``~~`~~~````~~`~ 2
#  3 `````~~``````~`~~~~~```~~``~~~`~`~~~~~~`````~`~```~~~``~``~` 3
#  4 ~~~`~~~`~`~~~``~~~`~`~``~~~~``~~~~``~~~~`~`~``~~```~``~~`~`~ 4
#  5 `~``~````~`~`~~``~~~~````X`~``X~~~~````````~``~~~`~~``~~```` 5
#  6 ~`~```~~`~~```~````````~~```~```~~~~``~~~`~`~~`~``~~~`~~`~`` 6
#  7 ~`~~~```~``~```~`~```~~~~~~~`~~`~`~~~~``~```~~~`~```~``~``~` 7
#  8 `~``~~`~`~~`~~`~~``~```~````~X~```~``~````~~~````~~``~~``~~` 8
#  9 ~`~``~~````~~```~`~~```~~`~``~`~~``~`~`~~~~`~`~~`~`~```~~``` 9
# 10 `~~~~~~`~``~``~~~``~``~~~X`~``~```~`~~``~~~~~~``````~~`~``~~ 10
# 11 ~``~~~````~`~~`~~~`~~~``~``````~`~``~~~~`````~~~``````~`~`~~ 11
# 12 ~~~~~``~`~````~```~`~`~`~~`~~`~``~~~~~~~`~~```~~``~~`~~~~``` 12
# 13 `~~```~~````````~~~`~~~```~~~~~~~~`~~``~~`~```~`~~````~~~``~ 13
# 14 ```~``~`~`~``~```~`~``~`~``~~```~`~~~``~~``~```~`~~`~``````~ 14
#    012345678901234567890123456789012345678901234567890123456789
#              1         2         3         4         5
# You have found a sunken treasure chest!
# You have 16 sonar device(s) left. 2 treasure chest(s) remaining.
# Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)
GRID_HIGHT = 15
GRID_WIDTH = 60

def ask_play_again():
    user_anwser = input('Do you want to play again? (Yes or No)')
    if user_anwser == 'No':
        return False
    else:
        return True

# make a grid variable useing a dubel list
def make_grid(grid):

    
    waves = ['~', '\'']
    # random_list = []
    # for i in range(3):
    #     random_list.append(randint(length, width))
        
    for i in range(GRID_HIGHT):
        grid.append([])
        for j in range(GRID_WIDTH):
            grid[i].append(choice(waves))
              

    # for i in range(3):
    #     grid[random_list[i]] = 'X'
    # return random_list

# # display grid 
def display_grid(grid):

    print('''              1         2         3         4         5
    012345678901234567890123456789012345678901234567890123456789''')
    for i in range(len(grid)):

        if i > 9:
            print(' ', end = '')
        else:
            print('  ', end = '')
        print(i, end = ' ')           
        
        for j in range(GRID_WIDTH):          
            print(grid[i][j], end = '')

        print(' ', end = '')
        print(i)

        
    print('''    012345678901234567890123456789012345678901234567890123456789
              1         2         3         4         5''')

def place_treasure(grid):

    y = []
    x = []
    treasure_chests = []
    for i in range(GRID_WIDTH):
        x.append(i)
    for i in range(GRID_HIGHT):
        y.append(i)

    shuffle(x)
    shuffle(y)
    for i in range(3):
        treasure_chests.append([y[i], x[i]])
    return treasure_chests

    
# calulate the distinse fron the sonar divise to the nerest tresure chest
# def calulate_distinse(user_guess_x, user_guess_y, chest_x, chest_y, 
#number_of_chests ):
def calulate_distanse(chest_y, chest_x, user_guess_y, user_guess_x):
    a = chest_x - user_guess_x
    b = chest_y - user_guess_y
    c = (a * a) + (b * b)
    c = sqrt(c)
    c =  round(c)
    #print(c)
    return c

def calulate_distanse_of_all_chests(all_chests_x, all_chests_y, user_guess_x, user_guess_y):

    distanses = []
    for i in range(len(all_chests_x)):
        distanses.append(calulate_distanse(all_chests_y[i], all_chests_x[i], user_guess_x, user_guess_y))

        #print(distanses[i])
    return min(distanses)
        
        
        
def ask_guess(number_of_sonars, number_of_chests, grid):
    user_guess = input(f''' You have {number_of_sonars} sonar device(s) left. {number_of_chests} treasure chest(s) remaining.
Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)\n''')

    if user_guess == 'quit':
        return False

    user_guess_x = []
    user_guess_y = []
    letter = ''
    counter = 0
    while True:
        letter = user_guess[counter]
        if letter != ' ':
            user_guess_x.append(letter)
        else:
            for i in range(user_guess_x):
                user_guess.pop(i)
            user_guess.pop(' ')
            user_guess_y.append(user_guess)

def change_to_x(grid, chest_x, chest_y):
    for i in range(len(grid)):
        for j in range(i):
            if j != '~' and j != '\'':
                j = 'X'
    for i in range(len(chest_x)):
        grid[chest_x[i]][chest_y[i]] = 'X'

def check_win(chest_x, chests_y, user_guess_y, user_guess_x, grid):
    for i in range(len(chest_x)):
        if chest_x[i] == user_guess_x and chests_y[i] == user_guess_y:
            change_to_x(grid, chest_x, chests_y)

def update_grid(chest_x, chest_y, user_guess_x, user_guess_y, grid):

    closest_chest = calulate_distanse_of_all_chests(chest_x, chest_y, user_guess_x, user_guess_y)
    print('''              1         2         3         4         5
    012345678901234567890123456789012345678901234567890123456789''')
    for i in range(len(grid)):

        if i > 9:
            print(' ', end = '')
        else:
            print('  ', end = '')
        print(i, end = ' ')           
        
        for j in range(GRID_WIDTH):
            if j == user_guess_y and i == user_guess_x:
                print(closest_chest)
            else:
                print(grid[i][j], end = '')

        print(' ', end = '')
        print(i)

        
    print('''    012345678901234567890123456789012345678901234567890123456789
              1         2         3         4         5''')    
            
            
# start game 
def start_new_game():
    print('S O N A R !')
    number_of_chests = 3
    number_of_sonars = 20
    
    fake_user_guess_x = 0
    fake_user_guess_y = 0
    chest_x = [40, 41, 42]
    chest_y = [40, 41, 42]
    
    grid = []
    random_list = make_grid(grid)
    update_grid(chest_x, chest_y, fake_user_guess_x, fake_user_guess_y, grid)
    # while True:

    #place_treasure(grid)
    #display_grid(grid)

    
    
    
    
    #     if check_win(number_of_chests):
    #          if ask_play_again():
    #              number_of_chests = 3
    #              number_of_sonars = 20
    #              grid = []
    #              random_list = make_grid(59, 14, grid)
    #          else:
    #              break
                
    #      ask_guess(number_of_chests, number_of_sonars, random_list)
    #      number_of_chests -= 1
    #      number_of_sonars -= 1        
            