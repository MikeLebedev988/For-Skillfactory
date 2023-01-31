import random as rnd

field_player = [['~'] * 6 for i in range(6)]
field_ai = [['0'] * 6 for _ in range(6)]


def show_field(f):
    print('  1  2  3  4  5  6')
    for i in range(len(f)):
        print(str(i + 1) + ' ' + '  '.join(f[i]))
    print('-------------------')


class Pos:
    def __init__(self):
        self.set_ship_x()
        self.set_ship_y()

    def set_ship_x(self):
        self.x = int(input("Enter 'x' coordinate:\n"))

    def get_ship_x(self):
        return self.x

    def set_ship_y(self):
        self.y = int(input("Enter 'y' coordinate:\n"))

    def get_ship_y(self):
        return self.y


class AiPos:
    def __init__(self):
        self.set_ship_x()
        self.set_ship_y()

    def set_ship_x(self):
        self.x = rnd.randint(0, 5)

    def get_ship_x(self):
        return self.x

    def set_ship_y(self):
        self.y = rnd.randint(0, 5)

    def get_ship_y(self):
        return self.y


# def set_ship1_on_field(f):
#     f[ship1_pos.x][ship1_pos.y] = '■'
#
#
# def set_ship2_on_field(f):
#     if ship2_pos.direct == 'h':
#         f[ship2_pos.x][ship2_pos.y], f[ship2_pos.x][ship2_pos.y + 1] = '■', '■'
#     else:
#         f[ship2_pos.x][ship2_pos.y], f[ship2_pos.x + 1][ship2_pos.y] = '■', '■'
#
#
# def set_ship3_on_field(f):
#     if ship3_pos.direct == 'h':
#         f[ship3_pos.x][ship3_pos.y], f[ship3_pos.x][ship3_pos.y + 1] = '■', '■'
#         f[ship3_pos.x][ship3_pos.y + 2] = '■'
#     else:
#         f[ship3_pos.x][ship3_pos.y], f[ship3_pos.x + 1][ship3_pos.y] = '■', '■'
#         f[ship3_pos.x + 2][ship3_pos.y] = '■'


class Ship:
    def __init__(self, quantity, length):
        self.length = length
        self.quantity = quantity

    def set_direct(self):
        self.direct = input("Enter your ship direction:\n")

    def get_direct(self):
        return self.direct


class AiShip(Ship):
    def __init__(self, quantity, length):
        super().__init__(quantity, length)

    def set_direct(self):
        self.direct = rnd.randint(0, 1)

    def get_direct(self):
        return self.direct


class GameField:
    def __init__(self, field_player):
        self.set_ship1_on_field(field_player)
        self.set_ship2_on_field(field_player)
        self.set_ship3_on_field(field_player)


    @staticmethod
    def set_ship1_on_field(field_player):
        ship1 = Ship(4, 1)
        for i in range(ship1.quantity):
            ship1_pos = Pos()
            field_player[ship1_pos.x][ship1_pos.y] = '■'
            show_field(field_player)

    @staticmethod
    def set_ship2_on_field(field_player):
        ship2 = Ship(2, 2)
        for i in range(ship2.quantity):
            ship2_pos = Pos()
            if ship2.length > 1:
                ship2.set_direct()
                if ship2.direct == 'h':
                    field_player[ship2_pos.x][ship2_pos.y], field_player[ship2_pos.x][ship2_pos.y + 1] = '■', '■'
                else:
                    field_player[ship2_pos.x][ship2_pos.y], field_player[ship2_pos.x + 1][ship2_pos.y] = '■', '■'
            show_field(field_player)

    @staticmethod
    def set_ship3_on_field(field_player):
        ship3 = Ship(1, 3)
        for i in range(ship3.quantity):
            ship3_pos = Pos()
            if ship3.length > 1:
                ship3.set_direct()
                if ship3.direct == 'h':
                    field_player[ship3_pos.x][ship3_pos.y], field_player[ship3_pos.x][ship3_pos.y + 1] = '■', '■'
                    field_player[ship3_pos.x][ship3_pos.y + 2] = '■'
                else:
                    field_player[ship3_pos.x][ship3_pos.y], field_player[ship3_pos.x + 1][ship3_pos.y] = '■', '■'
                    field_player[ship3_pos.x + 2][ship3_pos.y] = '■'
            show_field(field_player)


class AiGameField:
    def __init__(self, field_ai):
        self.set_ship1_ai_on_field(field_ai)
        self.set_ship2_ai_on_field(field_ai)
        self.set_ship3_ai_on_field(field_ai)

    @staticmethod
    def set_ship1_ai_on_field(field_ai):
        ship1_ai = AiShip(4, 1)
        for i in range(ship1_ai.quantity):
            ship1_ai_pos = AiPos()
            field_ai[ship1_ai_pos.x][ship1_ai_pos.y] = '■'
            show_field(field_ai)

    @staticmethod
    def set_ship2_ai_on_field(field_ai):
        ship2_ai = AiShip(2, 2)
        for i in range(ship2_ai.quantity):
            try:
                ship2_ai_pos = AiPos()
                if ship2_ai.length > 1:
                    ship2_ai.set_direct()
                    if ship2_ai.direct == 0:
                        field_ai[ship2_ai_pos.x][ship2_ai_pos.y], field_ai[ship2_ai_pos.x][ship2_ai_pos.y + 1] = '■', '■'
                    else:
                        field_ai[ship2_ai_pos.x][ship2_ai_pos.y], field_ai[ship2_ai_pos.x + 1][ship2_ai_pos.y] = '■', '■'
            except IndexError:
                print("Грёбанный кампухтер! Краёв не видишь?!")
            show_field(field_ai)

    @staticmethod
    def set_ship3_ai_on_field(field_ai):
        ship3_ai = AiShip(1, 3)
        for i in range(ship3_ai.quantity):
            try:
                ship3_ai_pos = AiPos()
                if ship3_ai.length > 1:
                    ship3_ai.set_direct()
                    if ship3_ai.direct == 0:
                        field_ai[ship3_ai_pos.x][ship3_ai_pos.y], field_ai[ship3_ai_pos.x][ship3_ai_pos.y + 1] = '■', '■'
                        field_ai[ship3_ai_pos.x][ship3_ai_pos.y + 2] = '■'
                    else:
                        field_ai[ship3_ai_pos.x][ship3_ai_pos.y], field_ai[ship3_ai_pos.x + 1][ship3_ai_pos.y] = '■', '■'
                        field_ai[ship3_ai_pos.x + 2][ship3_ai_pos.y] = '■'
            except IndexError:
                print('Грёбаный кампухтер! Краёв не видишь?!')
            show_field(field_ai)


# class GameField:
#     def __init__(self, ship1_quantity, ship2_quantity, ship3_quantity):


# We may declare this variable not now, but in a function when we need it.


players_gamefield = GameField(field_player)
ai_gamefield = AiGameField(field_ai)

# for i in range(ship1.quantity):
#     ship1_pos = Pos()
#     set_ship1_on_field(field)
# for i in range(ship2.quantity):
#     ship2_pos = Pos()
#     set_ship2_on_field(field)
# for i in range(ship3.quantity):
#     ship3_pos = Pos()
#     set_ship3_on_field(field)
