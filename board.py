"""Module encapsulating all Board vars, classes and functions."""

from copy import deepcopy
import constants
import functions


class Board(object):
    """Class that defines a the Board object for the game.

    Contains methods and attributes that flesh out the Board object.
    """

    def __init__(self):
        """Class initialization method instantiating empty board."""
        # set up and empty board to put ships on
        self.board = deepcopy(constants.EMPTY_BOARD)

    def update_board(self, ship_length, orientation, coordinates):
        """Class method allowing for updating of players board."""
        # seperate the coordiantes into a row and a column
        coordinates = coordinates.strip()
        orientation = orientation.strip()

        column = constants.VALID_LETTERS.index(coordinates[0])
        row = int(coordinates[1:]) - 1

        if orientation.lower() == 'h':
            # if orientation is 'h' replace the slice of the players board \
            # row with the horizontal ship marker
            self.board[row][column:(column + ship_length)] = \
                ['-' for num in range(ship_length)]

        if orientation.lower() == 'v':
            # if orientation is 'v' replace the slice of the players board \
            # with the vertical ship marker
            for board_row in range(row, (row + ship_length)):
                self.board[board_row][column] = '|'

    def get_board(self):
        """Get board list for iteration.

        Returns the raw list form of the players board.
        """
        return self.board

    def display(self):
        """Use print board to display the contents of the board.

        Use the print board function to display a stringified version
        of the players board for reference during the game
        """
        return functions.print_board(self.board)
