"""Module that executes the Battleship Game."""

import functions
from player import Player
import validation


class Battleship(object):
    """Battleship main game class definition."""

    def setup(self):
        """Setup Battleship."""
        # Players
        self.player_one = Player()
        self.player_two = Player("Player Two")

        self.player_one.set_up_board(self.player_two.name)
        self.player_two.set_up_board(self.player_one.name)

        functions.clear_screen()
        input('Please pass the board to {}, and look away.\n'
              'Press Enter to continue.'.format(self.player_one.name))

    def __init__(self):
        """Class initialization method."""
        functions.clear_screen()
        self.setup()

        while True:
            if validation.player_sunk(self.player_one, self.player_two):
                break

            self.player_one.shoot(self.player_two)
            self.player_two.shoot(self.player_one)

            # test = input('Clear Player One ships?')
            # if test == 'y':
            #     self.player_one.ships_list = []


Battleship()
