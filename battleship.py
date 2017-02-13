"""Module that executes the Battleship Game."""

import functions
from player import Player


class Battleship(object):
    """Battleship main game class definition."""

    def setup(self):
        """Setup Battleship."""
        # Players
        self.player_one = Player()
        self.player_two = Player("Player Two")

        self.player_one.turn(self.player_two.name)
        self.player_two.turn(self.player_one.name)

        input('Please pass the board to {}, and look away.\nPress Enter to continue.'.format(self.player_one.name))

    def __init__(self):
        """Class initialization method."""
        functions.clear_screen()
        self.setup()

        while True:
            self.player_one.shoot(self.player_two.name, self.player_two.board.get_board())
            self.player_two.shoot(self.player_one.name, self.player_one.board.get_board())


Battleship()
