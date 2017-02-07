from board import Board
from player import Player

class Battleship:

    SHIP_INFO = [
        ("Aircraft Carrier", 5),
        ("Battleship", 4),
        ("Submarine", 3),
        ("Cruiser", 3),
        ("Patrol Boat", 2)
    ]


# Instantiate Objects:
    # Player One
    player_one = Player()
    player_one_board = Board()
    # Player Two
    player_two = Player()
    player_two_board = Board()

    def clear_screen(self):
        print("\033c", end="")

    def __init__(self):
        self.clear_screen()
        player_one_name = self.player_one.get_name()
        player_two_name = self.player_two.get_name()

        print("{}'s Board\n".format(player_one_name))
        self.player_one_board.print_board()

        print("{}'s Board\n".format(player_two_name))
        self.player_two_board.print_board()

        player_one_carrier = input('Player One place ship: ')
        carrier_position = input('vertical or horizontal? ')

        self.player_two_board.place_ship(player_one_carrier, carrier_position, ('Air Carrier', 5))

        self.player_two_board.print_board()

Battleship()
