"""Module that executes the Battleship Game."""

from player import Player
import constants
import functions


class Battleship(object):
    """Battleship main game class definition."""

    # Instantiate Objects:
    def setup(self):
        """Setup Battleship."""
        # Players
        self.player_one = Player()
        self.player_two = Player()

        print("{}'s Board\n".format(self.player_one.name))
        self.player_one.board.print_board()

        print("{}'s Board\n".format(self.player_two.name))
        self.player_two.board.print_board()

        self.player_two.place_ships(constants.SHIP_INFO)

    def __init__(self):
        """Class initialization method."""
        functions.clear_screen()
        self.setup()


Battleship()
