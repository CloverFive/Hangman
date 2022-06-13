from random import randint
from random import choice

default = ' '
grid = {7: default, 8: default, 9: default, 4: default, 5: default, 6: default, 1: default, 2: default, 3: default}

def display_grid():
    print(f'''{grid[7]}|{grid[8]}|{grid[9]}
-+-+-
{grid[4]}|{grid[5]}|{grid[6]}
-+-+-
{grid[1]}|{grid[2]}|{grid[3]}''')

def take_turn_user(user_preference):

    while True:
        
        user_move = int(input('what is your move(1-9)\n'))
        if grid[user_move] == ' ':

            grid[user_move] = user_preference
            return

def check_posible_win(computer_simbol, checked_simbol):
    posible_winning_cominations = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 1], [7, 5, 3],  [9, 5, 1]]

    for i in posible_winning_cominations:
        
        if grid[i[0]] == checked_simbol and grid[i[1]] == checked_simbol and grid[i[2]] == ' ':
            grid[i[2]] = computer_simbol
            return True

        if grid[i[0]] == checked_simbol and grid[i[1]] == ' ' and grid[i[2]] == checked_simbol:
            grid[i[1]] = computer_simbol
            return True

        if grid[i[0]] == ' ' and grid[i[1]] == checked_simbol and grid[i[2]] == checked_simbol:
            grid[i[0]] = computer_simbol
            return True

def check_corner(computer_simbol):
    corners = [7, 9, 1, 3]
    posible_corners = []
    global grid
    
    for i in corners:
        if grid[i] == ' ':
            posible_corners.append(i) 

    grid[choice(posible_corners)] = computer_simbol

def take_turn_computer(computer_simbol, player_simbol):

    if check_posible_win(computer_simbol, computer_simbol):
        return

    elif check_posible_win(computer_simbol, player_simbol):
        return
        
    elif grid[5] == ' ':
        grid[5] = computer_simbol
        return
        
    elif grid[7] == ' ' or grid[9] == ' ' or grid[1] == ' ' or grid[3] == ' ':
        check_corner(computer_simbol)
        return
    else:

        posible_moves = []
        for i in range(9):
            if grid[i + 1] == ' ':
                posible_moves.append(i + 1)
        grid[choice(posible_moves)] = computer_simbol
        print(posible_moves)
        return    

        
def check_win(simbol):
    
    winning_combinations = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [7, 4, 1], [8, 5, 2], [9, 6, 1], [7, 5, 3],  [9, 5, 1]]
    
    for i in winning_combinations:
        if grid[i[0]] == simbol and grid[i[1]] == simbol and grid[i[2]] == simbol:
            return True

def check_grid_full():
    if grid[7] != ' ' and grid[8] != ' ' and grid[9] != ' ' and grid[4] != ' ' and grid[5] != ' ' and grid[6] != ' ' and grid[1] != ' ' and grid[2] != ' ' and grid[3] != ' ':
        return True

def start_new_game():

    user_preference = input('Do you want to be X or O\n')
    if user_preference == 'X':
        computer_simbol = 'O'
    else:
        computer_simbol = 'X'

    random_number = randint(1, 2)

    if random_number == 1:
        print('The computer is going first')
        while True:
            take_turn_computer(computer_simbol, user_preference)
            display_grid()
            print('\n')
            if check_win(computer_simbol):
                print('the computer won')
                break
            elif check_grid_full():
                print('its a tie')
                break

            take_turn_user(user_preference)
            display_grid()
            print('\n')
            if check_win(user_preference):
                print('the computer won')
                break
            elif check_grid_full():
                print('its a tie')
                break   

    if random_number == 2:

        print('You are going first')
        while True:
    
            take_turn_user(user_preference)
            display_grid()
            print('\n')
            if check_win(user_preference):
                print('the computer won')
                break
            elif check_grid_full():
                print('its a tie')
                break

            take_turn_computer(computer_simbol, user_preference)
            display_grid()
            print('\n')
            if check_win(computer_simbol):
                print('the computer won')
                break
            elif check_grid_full():
                print('its a tie')
                break