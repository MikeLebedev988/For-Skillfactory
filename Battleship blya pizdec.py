import random as rnd

field_player = [['~'] * 6 for i in range(6)]
field_ai = [['0'] * 6 for _ in range(7)]


def show_field(f):
    print('  1  2  3  4  5  6')
    for i in range(len(f)):
        print(str(i + 1) + ' ' + '  '.join(f[i]))
    print('-------------------')


field_ai[0][0] = 'x'
field_ai[1][0] = 'y'
field_ai[1][0-1] = 'p'
field_ai[1][0+1] = 'z'
field_ai[3][0], field_ai[4][0], field_ai[5][0] = 'g', 'g', 'g'
field_ai[3][0-1], field_ai[4][0-1], field_ai[5][0-1] = 'd', 'd', 'd'
show_field(field_ai)

#
# class Pos:
#     def __init__(self):
#         self.x = None
#         self.y = None
#         self.set_ship_x()
#         self.set_ship_y()
#
#     def set_ship_x(self):
#         self.x = int(input("Enter 'x' coordinate:\n"))
#
#     def get_ship_x(self):
#         return self.x
#
#     def set_ship_y(self):
#         self.y = int(input("Enter 'y' coordinate:\n"))
#
#     def get_ship_y(self):
#         return self.y
#
#
# class AiPos:
#     def __init__(self):
#         self.y = None
#         self.x = None
#         self.set_ship_x()
#         self.set_ship_y()
#
#     def set_ship_x(self):
#         self.x = rnd.randint(0, 5)
#
#     def get_ship_x(self):
#         return self.x
#
#     def set_ship_y(self):
#         self.y = rnd.randint(0, 5)
#
#     def get_ship_y(self):
#         return self.y
#
#
# class Ship:
#     def __init__(self, quantity, length):
#         self.direct = None
#         self.length = length
#         self.quantity = quantity
#
#     def set_direct(self):
#         self.direct = input("Enter your ship direction:\n")
#
#     def get_direct(self):
#         return self.direct
#
#
# class AiShip(Ship):
#     def __init__(self, quantity, length):
#         super().__init__(quantity, length)
#         self.direct = None
#
#     def set_direct(self):
#         self.direct = rnd.randint(0, 1)
#
#     def get_direct(self):
#         return self.direct
#
#
# class GameFieldPlayer:
#     def __init__(self, field_p):
#         self.set_ship1_on_field(field_p)
#         self.set_ship2_on_field(field_p)
#         self.set_ship3_on_field(field_p)
#
#     @staticmethod
#     def set_ship1_on_field(field_p):
#         ship1 = Ship(4, 1)
#         for i in range(ship1.quantity):
#             ship1_pos = Pos()
#             field_p[ship1_pos.x][ship1_pos.y] = '■'
#             show_field(field_p)
#
#     @staticmethod
#     def set_ship2_on_field(field_p):
#         ship2 = Ship(2, 2)
#         for i in range(ship2.quantity):
#             ship2_pos = Pos()
#             if ship2.length > 1:
#                 ship2.set_direct()
#                 if ship2.direct == 'h':
#                     field_p[ship2_pos.x][ship2_pos.y], field_p[ship2_pos.x][ship2_pos.y + 1] = '■', '■'
#                 else:
#                     field_p[ship2_pos.x][ship2_pos.y], field_p[ship2_pos.x + 1][ship2_pos.y] = '■', '■'
#             show_field(field_p)
#
#     @staticmethod
#     def set_ship3_on_field(field_p):
#         ship3 = Ship(1, 3)
#         for i in range(ship3.quantity):
#             ship3_pos = Pos()
#             if ship3.length > 1:
#                 ship3.set_direct()
#                 if ship3.direct == 'h':
#                     field_p[ship3_pos.x][ship3_pos.y], field_p[ship3_pos.x][ship3_pos.y + 1] = '■', '■'
#                     field_p[ship3_pos.x][ship3_pos.y + 2] = '■'
#                 else:
#                     field_p[ship3_pos.x][ship3_pos.y], field_p[ship3_pos.x + 1][ship3_pos.y] = '■', '■'
#                     field_p[ship3_pos.x + 2][ship3_pos.y] = '■'
#             show_field(field_p)
#
#
# count_index = 0
# count_else = 0
# count_put_ship1 = 4
# srabotka_f = 0
#
#
# def ship1_set_pos_and_set_on_field(ai_field):
#     global count_index, count_else, count_put_ship1
#     ship1_ai_pos = AiPos()
#     print(f"ship1_ai_pos.x , .y = {ship1_ai_pos.x, ship1_ai_pos.y}")
#     try:
#         if all((ai_field[ship1_ai_pos.x][ship1_ai_pos.y] == '0', ai_field[ship1_ai_pos.x][ship1_ai_pos.y - 1] == '0',
#                 ai_field[ship1_ai_pos.x][ship1_ai_pos.y + 1] == '0',
#                 ai_field[ship1_ai_pos.x - 1][ship1_ai_pos.y] == '0',
#                 ai_field[ship1_ai_pos.x + 1][ship1_ai_pos.y] == '0')):
#             ai_field[ship1_ai_pos.x][ship1_ai_pos.y] = '■'
#         else:
#             print("рядом корабль, ship1")
#     except IndexError:
#         print("Out of range, ship1.")
#
#
# def ship2_direct(ai_field):
#     ship2_ai_pos = AiPos()
#     if ship2_ai.length > 1:
#         ship2_ai.set_direct()
#         try:
#             if ship2_ai.direct == 0:
#                 if all((
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y + 1] == '0',
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y - 1] == '0',
#                         ai_field[ship2_ai_pos.x - 1][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x + 1][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x - 1][ship2_ai_pos.y + 1] == '0',
#                         ai_field[ship2_ai_pos.x + 1][ship2_ai_pos.y + 1] == '0',
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y + 2] == '0')):
#                     ai_field[ship2_ai_pos.x][ship2_ai_pos.y], ai_field[ship2_ai_pos.x][
#                         ship2_ai_pos.y + 1] = '■', '■'
#                     show_field(ai_field)
#                 else:
#                     print("ship2 рядом корабль?")
#                     return ship2_direct(ai_field)
#             elif ship2_ai.direct == 1:
#                 if all((
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x + 1][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x - 1][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x + 2][ship2_ai_pos.y] == '0',
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y - 1] == '0',
#                         ai_field[ship2_ai_pos.x][ship2_ai_pos.y + 1] == '0',
#                         ai_field[ship2_ai_pos.x + 1][ship2_ai_pos.y - 1] == '0',
#                         ai_field[ship2_ai_pos.x + 1][ship2_ai_pos.y + 1] == '0')):
#                     ai_field[ship2_ai_pos.x][ship2_ai_pos.y], ai_field[ship2_ai_pos.x + 1][
#                         ship2_ai_pos.y] = '■', '■'
#                     show_field(ai_field)
#                 else:
#                     print("ship2 рядом корабль?")
#                     return ship2_direct(ai_field)
#         except IndexError:
#             print("Out of range, ship2.")
#             return ship2_direct(ai_field)
#
#
# def ship2_set_pos_and_set_on_field(ai_field, ship2_dir):
#     ship2_dir(ai_field)
#
#
# def ship3_direct(ai_field):
#     ship3_ai_pos = AiPos()
#     if ship3_ai.length > 1:
#         ship3_ai.set_direct()
#         try:
#             if ship3_ai.direct == 0:
#                 if all((ai_field[ship3_ai_pos.x][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x][ship3_ai_pos.y + 1] == '0',
#                         ai_field[ship3_ai_pos.x][ship3_ai_pos.y + 2] == '0',
#                         ai_field[ship3_ai_pos.x][ship3_ai_pos.y + 3] == '0',
#                         ai_field[ship3_ai_pos.x][ship3_ai_pos.y - 1] == '0',
#                         ai_field[ship3_ai_pos.x - 1][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x - 1][ship3_ai_pos.y + 1] == '0',
#                         ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y + 1] == '0',
#                         ai_field[ship3_ai_pos.x - 1][ship3_ai_pos.y + 2] == '0',
#                         ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y + 2] == '0')):
#                     ai_field[ship3_ai_pos.x][ship3_ai_pos.y], ai_field[ship3_ai_pos.x][ship3_ai_pos.y + 1], \
#                      ai_field[ship3_ai_pos.x][ship3_ai_pos.y + 2] = '■', '■', '■'
#                     show_field(ai_field)
#                 else:
#                     print("ship3 рядом корабль?")
#                     return ship3_direct(ai_field)
#             if ship3_ai.direct == 1:
#                 if all((ai_field[ship3_ai_pos.x][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x + 2][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x - 1][ship3_ai_pos.y] == '0',
#                         ai_field[ship3_ai_pos.x][ship3_ai_pos.y - 1] == '0',
#                         ai_field[ship3_ai_pos.x][ship3_ai_pos.y + 1] == '0',
#                         ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y - 1] == '0',
#                         ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y + 1] == '0',
#                         ai_field[ship3_ai_pos.x + 2][ship3_ai_pos.y - 1] == '0',
#                         ai_field[ship3_ai_pos.x + 2][ship3_ai_pos.y + 1] == '0',
#                         ai_field[ship3_ai_pos.x + 3][ship3_ai_pos.y] == '0')):
#                     ai_field[ship3_ai_pos.x][ship3_ai_pos.y], \
#                      ai_field[ship3_ai_pos.x + 1][ship3_ai_pos.y], \
#                      ai_field[ship3_ai_pos.x + 2][ship3_ai_pos.y] = '■', '■', '■'
#                     show_field(ai_field)
#                 else:
#                     print("ship3 рядом корабль?")
#                     return ship3_direct(ai_field)
#         except IndexError:
#             print("Out of range, ship3.")
#             return ship3_direct(ai_field)
#
#
# def ship3_set_pos_and_set_on_field(ai_field, ship3_dir):
#     ship3_dir(ai_field)
#
#
# class AiGameField:
#     def __init__(self, ai_field):
#         self.ai_field = ai_field
#
#     @staticmethod
#     def set_ship1_ai_on_field(ai_field):
#         global srabotka_f
#         ship1_ai = AiShip(4, 1)
#         for i in range(ship1_ai.quantity):
#             ship1_set_pos_and_set_on_field(ai_field)
#             srabotka_f += 1
#             print(f"srabotka_f = {srabotka_f}")
#             show_field(ai_field)
#
#     @staticmethod
#     def set_ship2_ai_on_field(ai_field):
#         for i in range(ship2_ai.quantity):
#             ship2_set_pos_and_set_on_field(ai_field, ship2_direct)
#             show_field(ai_field)
#
#     @staticmethod
#     def set_ship3_ai_on_field(ai_field):
#         for i in range(ship3_ai.quantity):
#             ship3_set_pos_and_set_on_field(ai_field, ship3_direct)
#             show_field(ai_field)
#
#     def run(self):
#         self.set_ship3_ai_on_field(field_ai)
#         self.set_ship2_ai_on_field(field_ai)
#         self.set_ship1_ai_on_field(field_ai)
#
# # We may declare this variable not now, but in a function when we need it.
#
#
# ship3_ai = AiShip(1, 3)
# ship2_ai = AiShip(2, 2)
# ai_gamefield = AiGameField(field_ai)
# ai_gamefield.run()
# # players_gamefield = GameField(field_player)
