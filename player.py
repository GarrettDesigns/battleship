"""Module that contains all Player classes, vars and functions."""

from board import Board
import constants


class Player(object):
    """Define the player class."""

    def __init__(self, **kwargs):
        """Override class __init__ method."""
        self.name = input("Please enter your name: ").capitalize()
        self.board = Board()

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_ship_position(self, ship_name, ship_length):
        """Ask input from user on where to put each ship."""
        prompt = "{}, Choose a position for the {} ({} spaces):"

        ship_position = tuple(input(prompt.format(
            self.name, ship_name, ship_length)))

        column, row = ship_position

        if column not in constants.VALID_LETTERS:
            print("{}, is not a valid column valid lettered columns are {}"
                  .format(column, constants.VALID_LETTERS))
            self.get_ship_position(ship_name, ship_length)
        else:
            return ship_position

        # if row > constants.BOARD_SIZE:
        #     print('{} is not a valid row, valid rows are numbered 1-{}'
        #           .format(constants.BOARD_SIZE))

    def place_ships(self, ships):
        """Place user ships on board object.

        This method allowing players to run through a list of ships
        passed in and place each one simultaneously updating the players board.
        """
        for ship_name, ship_length in ships:
            location = self.get_ship_position(ship_name, ship_length)

            ship_orientation = input("{}, Please choose an orientation"
                                     " [V]ertical or [H]orizontal): "
                                     .format(self.name)).lower()

            ship_data = {"orientation":  ship_orientation,
                         "position": location, "ship_name": ship_name,
                         "ship_length": ship_length}

            # import pdb; pdb.set_trace()
            self.board.print_board(self.board.update_board(**ship_data))
