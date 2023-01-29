import random as rnd

field = [['~'] * 6 for _ in range(6)]
field2 = [['~'] * 6 for _ in range(6)]


def ship3(field):
    try:
        x, y = map(int, input('Enter the coordinates of the beginning of the ship(x/y).').split())
        ship_direction = input('Enter ship direction horizontally or vertically (h/v):\n')
        if ship_direction == 'h' and field[x][y] != '■':
            field[x][y] = '■'
            field[x][y+1] = '■'
            field[x][y+2] = '■'
        elif ship_direction == 'v' and field[x][y] != '■':
            field[x][y] = '■'
            field[x+1][y] = '■'
            field[x+2][y] = '■'
        else:
            print('The entered data is not correct.')
    except ValueError:
        print('The entered data is not correct.')
    except IndexError:
        print('Outside the board.')


def show_field(f):
    print('  1  2  3  4  5  6')
    for i in range(len(field)):
        print(str(i + 1) + ' ' + '  '.join(field[i]))


def show_field_2(f):
    print('  1  2  3  4  5  6')
    for i in range(len(field2)):
        print(str(i + 1) + ' ' + '  '.join(field2[i]))


def user_hit(f):
    while True:
        hit = input('Enter your coordinates x/y from 0 by 5:\n').split()
        if len(hit) != 2:
            print('Enter two coordinates.')
            continue

        if not(hit[0].isdigit() and hit[1].isdigit()):
            print('Enter numbers.')
            continue

        x, y = map(int, hit)
        if not(0 <= x < 6 and 0 <= y < 6):
            print('Out of range.')
            continue

        if field[x][y] == ('X' and 'T'):
            print('You have already shot there.')
            continue
        field[x][y] = 'X' if field[x][y] == '■' else 'T'
        break
    return x, y


def ai_hit(f):
    while True:
        x2, y2 = rnd.randint(0, 5), rnd.randint(0, 5)
        if field2[x2][y2] != '-' and '■':
            print('negative')
            continue
        break
    return x2, y2


ship3(field)
show_field(field)
ship3(field)
show_field(field)
ship3(field)
while True:
    # ship3(field2)
    show_field(field)
    # show_field_2(field2)
    x, y = user_hit(field)
    # field[x][y] = 'X' if field[x][y] == '■' else 'T'
    # x2, y2 = ai_hit(field2)
    # field2[x2][y2] = 'X' if field2[x2][y2] == '-' and '■' else 'T'

