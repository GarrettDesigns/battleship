"""Module encapsulating all Board vars, classes and functions."""

import constants
from copy import deepcopy
import functions


class Board(object):
    """Class that defines a the Board object for the game.

    Contains methods and attributes that flesh out the Board object.
    """

    def __init__(self):
        """Class initialization method instantiating empty board var."""
        self.board = deepcopy(constants.EMPTY_BOARD)

    def update_board(self, ship_length, orientation, coordinates):
        """Class method allowing for updating of players board."""
        column = constants.VALID_LETTERS.index(coordinates[0])
        row = int(coordinates[1:]) - 1

        if orientation.lower() == 'h':
            self.board[row][column:(column + ship_length)] = \
                ['-' for num in range(ship_length)]
        if orientation.lower() == 'v':
            for board_row in range(row, (row + ship_length)):
                self.board[board_row][column] = '|'

    def get_board(self):
        """Get board list for iteration."""
        return self.board

    def display(self):
        """Use print board to display the contents of the board."""
        return functions.print_board(self.board)
