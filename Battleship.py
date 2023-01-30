import random as rnd

field = [['o'] * 6 for _ in range(6)]
field2 = [['.'] * 6 for _ in range(6)]
field5 = [['~'] * 6 for _ in range(6)]


def show_field(f):
    print('  1  2  3  4  5  6')
    for i in range(len(field5)):
        print(str(i + 1) + ' ' + '  '.join(field5[i]))


class ShipPos:
    def __init__(self, x='', y='', direct='') -> None:
        self.x = x
        self.y = y
        self.direct = direct
        self.set_ship_pos()

    def set_ship_pos(self):
        self.x = int(input("Enter your ship 'x' coordinate:\n"))
        self.y = int(input("Enter your ship 'y' coordinate:\n"))
        self.direct = input("Enter your ship direction(h or v):\n")

    def get_ship_pos(self):
        return self.x, self.y, self.direct


ship2_pos = ShipPos()


class SetOfShipsQuantity:
    def __init__(self, ship1_quantity, ship2_quantity, ship3_quantity):
        self.ship1_quantity = ship1_quantity
        self.ship2_quantity = ship2_quantity
        self.ship3_quantity = ship3_quantity

    def set_ship2(self, ship2_pos):
        for i in range(self.ship2_quantity):
            ship2_pos.set_ship_pos()
            field5[ship2_pos.x][ship2_pos.x] = '■'
            if ship2_pos.direct == 'h':
                field5[ship2_pos.x][ship2_pos.y + 1] = '■'
            if ship2_pos.direct == 'v':
                field5[ship2_pos.x + 1][ship2_pos.y] = '■'


class GameField:
    def __init__(self, set_of_ships_quantity):
        self.set_of_ships_quantity = set_of_ships_quantity
        self.ship_on_field = show_field(field5)
        # self.set_ship1(ship1_pos)
        self.set_ship2(ship2_pos)
        # self.set_ship3(ship3_pos)

    def set_ship1(self, ship1_pos):
        for i in range(self.ship1_quantity):
            ship1_pos.x = int(input("Enter coordinates ship1 'x':\n"))
            ship1_pos.y = int(input("Enter coordinates ship1 'y':\n"))
            field5[ship1_pos.x][ship1_pos.y] = '■'

    def set_ship2(self, ship2_pos):
        for i in range(self.ship2_quantity):
            ship2_pos.x = int(input("Enter coordinates ship2 'x':\n"))
            ship2_pos.y = int(input("Enter coordinates ship2 'y':\n"))
            field5[ship2_pos.x][ship2_pos.y] = '■'
            if ship2_pos.direct == 'h':
                field5[ship2_pos.x][ship2_pos.y + 1] = '■'
            if ship2_pos.direct == 'v':
                field5[ship2_pos.x + 1][ship2_pos.y] = '■'

    def set_ship3(self, ship3_pos):
        for i in range(self.ship2_quantity):
            ship3_pos.x = int(input("Enter coordinates ship3 'x':\n"))
            ship3_pos.y = int(input("Enter coordinates ship3 'y':\n"))
            field5[ship3_pos.x][ship3_pos.y] = '■'
            if ship3_pos.direct == 'h':
                field5[ship3_pos.x][ship3_pos.y + 1] = '■'
                field5[ship3_pos.x][ship3_pos.y + 2] = '■'
            if ship3_pos.direct == 'v':
                field5[ship3_pos.x + 1][ship3_pos.y] = '■'
                field5[ship3_pos.x + 2][ship3_pos.y] = '■'

    def get_ship_on_field(self):
        return self.ship_on_field


players_set_of_ships = SetOfShipsQuantity(4, 2, 1)
players_gamefield = GameField(players_set_of_ships)
print(players_gamefield.ship_on_field)
print(players_set_of_ships.ship2_quantity)

# ai_set_of_ships = SetOfShips(ship1_pos=ShipPos(rnd.randint(0, 5), rnd.randint(0, 5), rnd.randint(0, 1)),
#                              ship2_pos=ShipPos(rnd.randint(0, 5), rnd.randint(0, 5), rnd.randint(0, 1)),
#                              ship3_pos=ShipPos(rnd.randint(0, 5), rnd.randint(0, 5), rnd.randint(0, 1)))
# ai_gamefield = GameField(ai_set_of_ships)
# print(ai_gamefield.ship_on_field)

# def ship3(field):
#     try:
#         x, y = map(int, input('Enter the coordinates of the beginning of the ship(x/y).').split())
#         ship_direction = input('Enter ship direction horizontally or vertically (h/v):\n')
#         if ship_direction == 'h' and field[x][y] != '■':
#             field[x][y] = '■'
#             field[x][y+1] = '■'
#             field[x][y+2] = '■'
#         elif ship_direction == 'v' and field[x][y] != '■':
#             field[x][y] = '■'
#             field[x+1][y] = '■'
#             field[x+2][y] = '■'
#         else:
#             print('The entered data is not correct.')
#     except ValueError:
#         print('The entered data is not correct.')
#     except IndexError:
#         print('Outside the board.')
#
#
# def show_field(f):
#     print('  1  2  3  4  5  6')
#     for i in range(len(field)):
#         print(str(i + 1) + ' ' + '  '.join(field[i]))
#
#
# def show_field_2(f):
#     print('  1  2  3  4  5  6')
#     for i in range(len(field2)):
#         print(str(i + 1) + ' ' + '  '.join(field2[i]))
#
#
# def user_hit(f):
#     global x, y
#     while True:
#         hit = input('Enter your coordinates x/y from 0 by 5:\n').split()
#         if len(hit) != 2:
#             print('Enter two coordinates.')
#             continue
#
#         if not(hit[0].isdigit() and hit[1].isdigit()):
#             print('Enter numbers.')
#             continue
#
#         x, y = map(int, hit)
#         if not(0 <= x < 6 and 0 <= y < 6):
#             print('Out of range.')
#             continue
#
#         if field[x][y] == ('X' and 'T'):
#             print('You have already shot there.')
#             continue
#         field[x][y] = 'X' if field[x][y] == '■' else 'T'
#         break
#     return x, y
#
#
# def ai_hit(f):
#     while True:
#         x2, y2 = rnd.randint(0, 5), rnd.randint(0, 5)
#         if field2[x2][y2] != '-' and '■':
#             print('negative')
#             continue
#         break
#     return x2, y2
#
#
# ship3(field)
# while True:
#     # ship3(field2)
#     show_field(field)
#     # show_field_2(field2)
#     x, y = user_hit(field)
#     # field[x][y] = 'X' if field[x][y] == '■' else 'T'
#     # x2, y2 = ai_hit(field2)
#     # field2[x2][y2] = 'X' if field2[x2][y2] == '-' and '■' else 'T'
