from board import Board
from player import Player


SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]


class Battleship:

    # Instantiate Objects:
    # Player One
    player_one = Player(input('What is your name: '))
    player_one_board = Board()

    # Player Two
    player_two = Player(input('What is your name: '))
    player_two_board = Board()

    def __init__(self):
        self.clear_screen()
        # player_one_name = self.player_one.get_name()
        # player_two_name = self.player_two.get_name()
        #
        # print("{}'s Board\n".format(player_one_name))
        self.player_one_board.print_board()
        #
        # print("{}'s Board\n".format(player_two_name))
        self.player_two_board.print_board()

        self.player_two.place_ships(SHIP_INFO)

        print("Updated Board")
        self.player_two_board.print_board(self.player_two_board.board)

        print("Board List")
        print(self.player_two_board.board)

    def clear_screen(self):
        print("\033c", end="")


Battleship()
