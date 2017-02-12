"""Module that executes the Battleship Game."""

from board import Board
import constants
import functions
from player import Player
import validation


class Battleship(object):
    """Battleship main game class definition."""


    # Instantiate Objects:
    def setup(self):
        """Setup Battleship."""
        # Players

        functions.clear_screen()
        self.player_one = Player()
        functions.clear_screen()
        input('Battlestations {}!'
              '\nPrepare to take command of your fleet!'
              '\n\nPress Enter to continue'.format(self.player_one.name))

        player_one_board = Board()

        functions.clear_screen()
        self.player_two = Player("Player Two")
        functions.clear_screen()

        input('Battlestations {}!'
              '\nPrepare to take command of your fleet!'
              '\n\nPress Enter to continue'.format(self.player_two.name))

        player_two_board = Board()

        functions.clear_screen()
        player_one_board.print_board()
        player_two_board.print_board()

        input('Players will now set up their boards.'
              ' Please hand the computer to {}.'
              '\nPrepare to launch your fleet!'
              '\n\nPress Enter to Continue'.format(self.player_one.name))
        functions.clear_screen()
        self.player_one.place_ships(constants.SHIP_INFO, player_one_board)

        input('Please hand the computer to {}.'
              ' Prepare to launch your fleet!'
              ' \n\nPress Enter to Continue'.format(self.player_two.name))
        self.player_two.place_ships(constants.SHIP_INFO, player_two_board)

    def __init__(self):
        """Class initialization method."""
        functions.clear_screen()
        self.setup()


Battleship()
