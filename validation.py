"""Module containing methods for performing player input validation."""

import constants


def ship_exists(self, ship_name, ship_length, position, orientation):
    """Check if a ship already occupies position of player input."""
    column = constants.VALID_LETTERS.index(position[0])
    row = int(position[1:]) - 1

    if orientation.lower() == 'h':
        if constants.HORIZONTAL_SHIP and constants.VERTICAL_SHIP in \
                self.board[row][column:(column + ship_length)]:
            return True
        else:
            return False

    if orientation.lower() == 'v':
        v_pos = list()

        for board_row in range(row, (row + ship_length)):
            v_pos.append(self.board[board_row][column])

        if constants.HORIZONTAL_SHIP and constants.VERTICAL_SHIP in v_pos:
            return True
        else:
            return False


def are_valid_coordinates(self, ship_coordinates):
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


def is_valid_orientation(self, ship_orientation):
    """Check for valid orientation input."""
    if ship_orientation not in 'hv':
        print('{} is not a valid orientation,'
              'please enter either "h" or "v"'.format(ship_orientation))
        return False
    else:
        return True


def collision(self, ship_name, ship_length,
              coordinates, orientation, board):
    """Check if ship collides with another ship.

    Check for existence of a ship on board at passed in coordinates.
    If there is return an error message and a False value.
    """
    if board.ship_exists(ship_name,
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
