"""Module that executes the Battleship Game."""

from player import Player
import constants


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

    def clear_screen(self):
        """Function that provides a clear screen for program."""
        print("\033c", end="")

    def __init__(self):
        """Class initialization method."""
        self.clear_screen()
        self.setup()


Battleship()
