"""Module that contains all Player classes, vars and functions."""

from board import Board
import functions
import constants


class Player(object):
    """Define the player class."""

    def get_ship_coordinates(self, ship_name, ship_length):
        """Ask input from user on where to put each ship."""
        prompt = "{}, Choose a position for the {} ({} spaces):"
        ship_coordinates = input(prompt.format(
            self.name, ship_name, ship_length))
        if self.are_valid_coordinates(ship_coordinates, ship_length):
            return ship_coordinates
        else:
            return self.get_ship_coordinates(ship_name, ship_length)

    def are_valid_coordinates(self, ship_coordinates, ship_length):
        """Check if ship coordinates are valid."""
        if len(ship_coordinates) > 3:
            print('{}, {} is not a valid entry. '
                  'Please enter a column ({}-{}) and a row (1-{}), ex. "h4"'
                  .format(self.name, ship_coordinates,
                          constants.BOARD_HEADING[0],
                          constants.BOARD_HEADING[(constants.BOARD_SIZE - 1)],
                          constants.BOARD_SIZE))
            return False

        if len(ship_coordinates) < 2:
            print('{}, you must enter at least one column (letter)'
                  'and one row (number), ex. "b8"'.format(self.name))
            return False
        else:
            column = ship_coordinates[0]
            row = int(ship_coordinates[1:])

        if column not in constants.VALID_LETTERS:
            print("{}, {} is not a valid column valid lettered columns are {}"
                  .format(self.name, column, constants.VALID_LETTERS))
            return False
        elif row > constants.BOARD_SIZE:
            print('{}, {} is not a valid row, valid rows are numbered 1-{}'
                  .format(self.name, row, constants.BOARD_SIZE))
            return False
        else:
            return True

    def get_ship_orientation(self):
        """Method to get ship orientation input from player."""
        ship_orientation = input("{}, Please choose an orientation"
                                 " [V]ertical or [H]orizontal): "
                                 .format(self.name)).lower()
        if self.is_valid_orientation(ship_orientation):
            return ship_orientation
        else:
            return self.get_ship_orientation()

    def is_valid_orientation(self, ship_orientation):
        """Check for valid orientation input."""
        if ship_orientation not in 'hv':
            print('{} is not a valid orientation,'
                  'please enter either "h" or "v"'.format(ship_orientation))
            return False
        else:
            return True

    def collision(self, ship_name, ship_length, coordinates, orientation):
        """Check if ship collides with another ship."""
        if self.board.ship_exists(ship_name,
                                  ship_length,
                                  coordinates,
                                  orientation):
            print('Sorry, {} cannot be placed,'
                  'you already have a ship there,'
                  'please choose another location'.format(ship_name))
            return True
        else:
            return False

    def out_of_bounds(self, ship_length, coordinates, orientation):
        """Check if ship is outside of game board."""
        if orientation == 'v':
            if (ship_length + int(coordinates[1:]) - 1) > constants.BOARD_SIZE:
                print('That ship exceeds the board size.'
                      'Please choose another location or orientation')
                return True
            else:
                return False
        if orientation == 'h':
            if (ship_length +
                    constants.VALID_LETTERS.index(coordinates[0])) > \
                    constants.BOARD_SIZE:
                print('That ship exceeds the board size.'
                      'Please choose another location or orientation')
                return True
            else:
                return False

    def place_ships(self, ships):
        """Place user ships on board object.

        This method allowing players to run through a list of ships
        passed in and place each one simultaneously updating the players board.
        """
        for ship_name, ship_length in ships:
            while True:

                coordinates = self.get_ship_coordinates(ship_name, ship_length)
                orientation = self.get_ship_orientation()

                if self.collision(ship_name, ship_length, coordinates, orientation):
                    continue

                if self.out_of_bounds(ship_length, coordinates, orientation):
                    continue

                break

            ship_data = {"orientation":  orientation,
                         "position": coordinates, "ship_name": ship_name,
                         "ship_length": ship_length}

            functions.clear_screen()

            self.board.print_board(self.board.update_board(**ship_data))

    def __init__(self, **kwargs):
        """Override class __init__ method."""
        self.name = input("Please enter your name: ").capitalize()
        self.board = Board()

        for key, value in kwargs.items():
            setattr(self, key, value)
