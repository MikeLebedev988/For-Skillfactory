# What is required of us?:
# 1) Create game tic-tac-toe... For this we need:
# Divide game by two players moves. == Through the functions... and conditionals constructions.
# Be able to input cross and zeroes in a field by "input" by index of list in list.
# Change values in list by assigning variables?
# Field is a matrix... May be... Very similar to and I saw this in slack...
# We will be moving from simple to hard.
# while - all moves not is done
# continue - after next player move
# break - if all field is full
# roll to choose who is player first
# if your solution is too big, it is not bad. take it and then think about how to minimize it.
#

import time

a = [
    ['0', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]

move_history = []


def first_player_move(x):
    print(f'{first_player_name} moves.')
    try:
        h = int(input('Enter the horizontal coordinates  first(1-3):\n'))
        v = int(input('and then vertical(1-3):\n'))
        if (str(h) + str(v)) not in move_history:
            move_history.append(str(h) + str(v))
            # print(f"Move history: {move_history}.")
            if (1 <= h <= 3) and (1 <= v <= 3):
                if h == 1:
                    if v == 1:
                        x[1][1] = 'x'
                    elif v == 2:
                        x[2][1] = 'x'
                    else:
                        x[3][1] = 'x'
                if h == 2:
                    if v == 1:
                        x[1][2] = 'x'
                    elif v == 2:
                        x[2][2] = 'x'
                    else:
                        x[3][2] = 'x'
                if h == 3:
                    if v == 1:
                        x[1][3] = 'x'
                    elif v == 2:
                        x[2][3] = 'x'
                    else:
                        x[3][3] = 'x'
            else:
                print('_________________________________________________')
                print("Values do not satisfy the conditions. Try again.")
                print('_________________________________________________')
                return first_player_move(x)
        else:
            print('_________________________________________________')
            print("This move is not allowed, because it has already happened."
                  " Try again.")
            print('_________________________________________________')
            return first_player_move(x)
    except ValueError:
        print('_________________________________________________')
        print("Values do not satisfy the conditions. Try again.")
        print('_________________________________________________')
        return first_player_move(x)


def second_player_move(x):
    print(f'{second_player_name} moves.')
    try:
        h = int(input('Enter the horizontal coordinates  first(1-3):\n'))
        v = int(input('and then vertical(1-3):\n'))
        if (str(h) + str(v)) not in move_history:
            move_history.append(str(h) + str(v))
            # print(f"Move history: {move_history}.")
            if (1 <= h <= 3) and (1 <= v <= 3):
                if h == 1:
                    if v == 1:
                        x[1][1] = 'o'
                    elif v == 2:
                        x[2][1] = 'o'
                    else:
                        x[3][1] = 'o'
                if h == 2:
                    if v == 1:
                        x[1][2] = 'o'
                    elif v == 2:
                        x[2][2] = 'o'
                    else:
                        x[3][2] = 'o'
                if h == 3:
                    if v == 1:
                        x[1][3] = 'o'
                    elif v == 2:
                        x[2][3] = 'o'
                    else:
                        x[3][3] = 'o'
            else:
                print('_________________________________________________')
                print("Values do not satisfy the conditions. Try again.")
                print('_________________________________________________')
                return second_player_move(x)
        else:
            print('_________________________________________________')
            print("This move is not allowed, because it has already happened."
                  " Try again.")
            print('_________________________________________________')
            return second_player_move(x)
    except ValueError:
        print('_________________________________________________')
        print("Values do not satisfy the conditions. Try again.")
        print('_________________________________________________')
        return second_player_move(x)


def game_cycle():
    while True:
        if '-' in (*a[1][1:4], *a[2][1:4], *a[3][1:4]):
            first_player_move(a)
            time.sleep(0.5)
            print(f'{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n')
            if any([('xxx' == a[1][1] + a[2][1] + a[3][1]), ('xxx' == a[1][2] + a[2][2] + a[3][2]),
                    ('xxx' == a[1][3] + a[2][3] + a[3][3]), ('xxx' == a[1][1] + a[2][2] + a[3][3]),
                    ('xxx' == a[3][1] + a[2][2] + a[1][3]), ('xxx' == a[1][1] + a[1][2] + a[1][3]),
                    ('xxx' == a[2][1] + a[2][2] + a[2][3]), ('xxx' == a[3][1] + a[3][2] + a[3][3])]):
                print(f'Congratulations, {first_player_name}! You WIN!')
                time.sleep(5)
                break

        if '-' in (*a[1][1:4], *a[2][1:4], *a[3][1:4]):
            second_player_move(a)
            time.sleep(0.5)
            print(f'{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n')
        else:
            print('Game is over. Friendship WINS!')
            time.sleep(5)
            break
        if any([('ooo' == a[1][1] + a[2][1] + a[3][1]), ('ooo' == a[1][2] + a[2][2] + a[3][2]),
                ('ooo' == a[1][3] + a[2][3] + a[3][3]), ('ooo' == a[1][1] + a[2][2] + a[3][3]),
                ('ooo' == a[3][1] + a[2][2] + a[1][3]), ('ooo' == a[1][1] + a[1][2] + a[1][3]),
                ('ooo' == a[2][1] + a[2][2] + a[2][3]), ('ooo' == a[3][1] + a[3][2] + a[3][3])]):
            print(f'Congratulations, {second_player_name}! You WIN!')
            time.sleep(5)
            break


def decorator(func):
    def wrapper():
        greet_ = func()
        edging = ''
        edging += '-' * (len(greet_) + 2)
        edging += f'\n|{greet_}|\n'
        edging += '-' * (len(greet_) + 2)
        return edging

    return wrapper


@decorator
def greetings():
    return 'Welcome to game - tic-tac-toe'


print(greetings())
start_game = input('Do you want to start the game? y/n\n')
if start_game == 'y':
    first_player_name = input('Please enter first player name:\n')
    print(f'Glad to see you, {first_player_name}.\n')
    second_player_name = input('Please enter second player name:\n')
    print(f'Glad to see you too, {second_player_name}.\n')
    time.sleep(0.5)
    print("So, let's begin.")
    print(f'{a[0]}\n{a[1]}\n{a[2]}\n{a[3]}\n')
    game_cycle()
else:
    print('See you soon.\n'
          'Good bye!')
    time.sleep(2)
    quit()
quit()
