from random import randint


class BoardException(Exception):
    pass


class BoardOutException(BoardException):
    def __str__(self):
        return "You are trying to shoot outside the board"


class BoardUsedException(BoardException):
    def __str__(self):
        return "You have already shooted in this cell."


class BoardWrongShipException(BoardException):
    pass


class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Pos({self.x}, {self.y})"


a = Pos(3, 4)


class Ship:
    def __init__(self, pos, length, direct):
        self.pos = pos
        self.length = length
        self.direct = direct
        self.lives = length

    @property
    def positions(self):
        ship_positions = []
        for i in range(self.length):
            cur_x = self.pos.x
            cur_y = self.pos.y

            if self.direct == 0:
                cur_x += i

            elif self.direct == 1:
                cur_y += i

            ship_positions.append(Pos(cur_x, cur_y))
        return ship_positions

    def shooten(self, shot):
        return shot in self.positions


class Board:
    def __init__(self, hide=False, size=6):
        self.size = size
        self.hide = hide

        self.count_of_destroyed_ships = 0

        self.field = [['~']*size for _ in range(size)]

        self.occupied_cells = []
        self.ships_on_field = []

    def __str__(self):
        res = ""
        res += "  1  2  3  4  5  6"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} {'  '.join(row)}"

        if self.hide:
            res = res.replace("■", "~")
        return res

    def out_of_board(self, pos):
        return not((0 <= pos.x < self.size) and (0 <= pos.y < self.size))

    def contour(self, ship, verb=False):
        around = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for pos_ship in ship.positions:
            for posx, posy in around:
                cur = Pos(pos_ship.x + posx, pos_ship.y + posy)
                if not(self.out_of_board(cur)) and cur not in self.occupied_cells:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.occupied_cells.append(cur)

    def add_ship(self, ship):
        for d in ship.positions:
            if self.out_of_board(d) or d in self.occupied_cells:
                raise BoardWrongShipException()
        for d in ship.positions:
            self.field[d.x][d.y] = "■"
            self.occupied_cells.append(d)

        self.ships_on_field.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out_of_board(d):
            raise BoardOutException

        if d in self.occupied_cells:
            raise BoardUsedException

        self.occupied_cells.append(d)

        for ship in self.ships_on_field:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count_of_destroyed_ships += 1
                    self.contour(ship, verb=True)
                    print("Ship destroyed!")
                    return False
                else:
                    print("Ship is damaged.")
                    return True

        self.field[d.x][d.y] = "."
        print("Missed!")
        return False

    def begin(self):
        self.occupied_cells = []

    def defeat(self):
        return self.count_of_destroyed_ships == len(self.ships_on_field)


class Player:
    def __init__(self, own_board, enemy_board):
        self.own_board = own_board
        self.enemy_board = enemy_board

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy_board.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Pos(randint(0, 5), randint(0, 5))
        print(f"Ai move: {d.x+1} {d.y +1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("Enter your coordinates:\n").split()

            if len(cords) != 2:
                print("Enter two coordinates.")
                continue

            x, y = cords

            if not(x.isdigit()) or not(y.isdigit()):
                print("Enter numbers!")
                continue

            x, y = int(x), int(y)

            return Pos(x - 1, y - 1)


class Game:
    def __init__(self, size=6):
        self.size = size
        own_board = self.random_board()
        enemy_board = self.random_board()
        enemy_board.hide = True

        self.ai = AI(own_board, enemy_board)
        self.us = User(own_board, enemy_board)

    def try_board(self):
        lengths_of_ships = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lengths_of_ships:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Pos(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def decorator(func):
        def wrapper():
            greet_ = func()
            edging = ''
            edging += f"|{'-' * (len(greet_))}|"
            edging += f'\n|{greet_}|\n'
            edging += f"|{'-' * len(greet_)}|\n"
            edging += f"|Input format: x y                |\n"
            edging += f"|x - columns                      |\n"
            edging += f"|y - rows                         |\n"
            edging += f"|{'-' * (len(greet_))}|\n"
            return edging

        return wrapper

    @staticmethod
    @decorator
    def greetings():
        return 'Welcome to the game - Battleship!'

    def loop(self):
        num = 0
        while True:
            print("-"*20)
            print("Your board:")
            print(self.us.own_board)
            print("-" * 20)
            print("Your opponent's board:")
            print(self.ai.own_board)
            print("-" * 20)
            if num % 2 == 0:
                print("User move.")
                repeat = self.us.move()
            else:
                print("AI move.")
                repeat = self.ai.move()

            if repeat:
                num -= 1

            if self.ai.own_board.defeat():
                print("-"*20)
                print("User WINS!")
                print(self.ai.own_board)
                break

            if self.us.own_board.defeat():
                print("-" * 20)
                print("AI WINS!")
                break
            num += 1

    def start(self):
        self.greetings()
        self.loop()


g = Game()
g.start()
