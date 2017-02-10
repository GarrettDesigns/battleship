"""Module that contains all Player classes, vars and functions."""

from board import Board
import constants


class Player(object):
    """Define the player class."""

    def get_ship_coordinates(self, ship_name, ship_length):
        """Ask input from user on where to put each ship."""
        prompt = "{}, Choose a position for the {} ({} spaces):"

        ship_coordinates = input(prompt.format(
            self.name, ship_name, ship_length))

        if len(ship_coordinates) != 2:
            print('{}, {} is not a valid entry.'
                  'Please enter a column and a row, ex. "h4"'
                  .format(self.name, ship_coordinates))
            return self.get_ship_coordinates(ship_name, ship_length)
        else:
            column, row = tuple(ship_coordinates)

        if column not in constants.VALID_LETTERS:
            print("{}, {} is not a valid column valid lettered columns are {}"
                  .format(self.name, column, constants.VALID_LETTERS))
            return self.get_ship_coordinates(ship_name, ship_length)
        elif int(row) > constants.BOARD_SIZE:
            print('{}, {} is not a valid row, valid rows are numbered 1-{}'
                  .format(self.name, constants.BOARD_SIZE))
            return self.get_ship_coordinates(ship_name, ship_length)
        else:
            return ship_coordinates

    def get_ship_orientation(self):
        """Method to get ship orientation input from player."""
        ship_orientation = input("{}, Please choose an orientation"
                                 " [V]ertical or [H]orizontal): "
                                 .format(self.name)).lower()

        if ship_orientation not in 'hv':
            print('{} is not a valid orientation,'
                  'please enter either "h" or "v"'.format(ship_orientation))
            return self.get_ship_orientation()
        else:
            return ship_orientation

        # space_for_ship = (constants.BOARD_SIZE - constants.VALID_LETTERS.index(ship_coordinates)) + ship_length

    def place_ships(self, ships):
        """Place user ships on board object.

        This method allowing players to run through a list of ships
        passed in and place each one simultaneously updating the players board.
        """
        for ship_name, ship_length in ships:
            ship_coordinates = self.get_ship_coordinates(
                                                        ship_name, ship_length)

            ship_orientation = self.get_ship_orientation()

            ship_data = {"orientation":  ship_orientation,
                         "position": ship_coordinates, "ship_name": ship_name,
                         "ship_length": ship_length}

            self.board.print_board(self.board.update_board(**ship_data))

        # if HORIZONTAL_SHIP and VERTICAL_SHIP not in \
        #         self.board[row][column:(column + ship_length)]:
        # else:
        #     print('Sorry, {} cannot be placed, '
        #           'you already have a ship there,'
        #           ' please choose another location'.format(ship_name))
        # v_pos = list()
        # for board_row in range(row, (row + ship_length)):
        #     v_pos.append(self.board[board_row][column])
        #
        # if HORIZONTAL_SHIP and VERTICAL_SHIP not in v_pos:
        # else:
        #     print('Sorry, {} cannot be placed, '
        #           'you already have a ship there,'
        #           ' please choose another location'.format(ship_name))
            # import pdb; pdb.set_trace()

    def __init__(self, **kwargs):
        """Override class __init__ method."""
        self.name = input("Please enter your name: ").capitalize()
        self.board = Board()

        for key, value in kwargs.items():
            setattr(self, key, value)
