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
    # Board
    initial_board = Board().create_board(EMPTY)
    # Player One
    player_one = Player()
    # Player Two
    player_two = Player()

    def clear_screen(self):
        print("\033c", end="")

    def __init__(self):
        self.clear_screen()

Battleship()
