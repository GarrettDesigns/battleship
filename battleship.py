"""Module that executes the Battleship Game."""

import functions
from player import Player
import validation


class Battleship(object):
    """Battleship main game class definition."""

    def play_battleship(self):
        """Method to start main battleship game.

        Calling this method initializes players taking turns.
        """
        while True:
            if validation.player_sunk(self.player_one, self.player_two):
                break

            self.player_one.shoot(self.player_two)
            self.player_two.shoot(self.player_one)

    def __init__(self):
        """Class initialization method.

        Set up Battleship players and game boards.
        """
        functions.clear_screen()

        # Players
        self.player_one = Player()
        self.player_two = Player("Player Two")

        self.player_one.set_up_board(self.player_two.name)
        self.player_two.set_up_board(self.player_one.name)

        functions.clear_screen()
        input('Please pass the board to {}, and look away.\n'
              'Press Enter to continue.'.format(self.player_one.name))

        self.play_battleship()

# Make sure script can't be executed when imported
if __name__ == '__main__':
    Battleship()
