"""Module containing methods for performing player input validation."""

import constants
import functions


def ship_exists(ship_name, board, ship_length, coordinates, orientation):
    """Check if a ship already occupies position of player input."""
    column = constants.VALID_LETTERS.index(coordinates[0])
    row = int(coordinates[1:]) - 1

    if orientation.lower() == 'h':
        if constants.HORIZONTAL_SHIP in board[row][column:(column + ship_length)] or constants.VERTICAL_SHIP in \
                board[row][column:(column + ship_length)]:
            return True
        else:
            return False

    if orientation.lower() == 'v':
        v_pos = list()

        try:
            for row in range(row, (row + ship_length)):
                v_pos.append(board[row][column])
        except IndexError:
            return None

        if constants.HORIZONTAL_SHIP in v_pos \
                or constants.VERTICAL_SHIP in v_pos:
            return True
        else:
            return False


def hit_or_miss(coordinates, board):
    """Check whether player shot is a hit or miss."""
    column = constants.VALID_LETTERS.index(coordinates[0])
    row = int(coordinates[1:]) - 1

    if board[row][column] == '-' or board[row][column] == '|':
        functions.clear_screen()
        print('***********\n*** HIT ***\n***********')
        return True
    else:
        functions.clear_screen()
        print('************\n*** MISS ***\n************')
        return False


def is_valid_shot(shot, shot_list):
    """Define logic to ensure the player doesn't shoot the same spot twice."""
    if shot not in shot_list:
        return True
    else:
        functions.clear_screen()
        return False


def are_valid_coordinates(coords, player_board, shots_board):
    """Check if ship coordinates are valid."""
    if len(coords) > 3:
        functions.clear_screen()
        if shots_board:
            shots_board.display()
        player_board.display()
        print('\n{} is not a valid entry. '
              'Please enter a column ({}-{}) and a row (1-{}), ex. "h4"'
              .format(coords,
                      constants.BOARD_HEADING[0],
                      constants.BOARD_HEADING[(constants.BOARD_SIZE - 1)],
                      constants.BOARD_SIZE))
        return False

    if len(coords) < 2 or coords == '':
        functions.clear_screen()
        if shots_board:
            shots_board.display()
        player_board.display()
        print('\nYou must enter at least one column (letter)'
              'and one row (number), ex. "b8"')
        return False
    else:
        column = coords[0]
        try:
            row = int(coords[1:])
        except ValueError:
            functions.clear_screen()
            row = coords[1:]
            if shots_board:
                shots_board.display()
            player_board.display()
            print('\n{} is not a valid row, valid rows are numbered 1-{}'
                  .format(row, constants.BOARD_SIZE))
            return False

    if column not in constants.VALID_LETTERS:
        functions.clear_screen()
        if shots_board:
            shots_board.display()
        player_board.display()
        print("\n{} is not a valid column valid lettered columns are {}"
              .format(column, constants.VALID_LETTERS))
        return False

    if row > constants.BOARD_SIZE:
        functions.clear_screen()
        if shots_board:
            shots_board.display()
        player_board.display()
        print('\n{} is not a valid row, valid rows are numbered 1-{}'
              .format(row, constants.BOARD_SIZE))
        return False

    return True


def is_valid_orientation(ship_orientation, player_board):
    """Check for valid orientation input."""
    if ship_orientation not in 'hv' or ship_orientation == '':
        functions.clear_screen()
        player_board.display()
        print('\n{} is not a valid orientation,'
              'please enter either "h" or "v"'.format(ship_orientation))
        return False
    else:
        return True


def player_sunk(player_one, player_two):
    """Detect if either player has lost all of their ships."""
    if not player_one.ships_list:
        print('**************\n*** WINNER ***\n**************')
        print("{} has sunk {}'s Battleship!"
              .format(player_two.name, player_one.name))
        return True

    if not player_two.ships_list:
        print('**************\n*** WINNER ***\n**************')
        print("{} has sunk {}'s Battleship!"
              .format(player_one.name, player_two.name))
        return True

    return False


def collision(player_board, ship_name, board, ship_length,
              coordinates, orientation):
    """Check if ship collides with another ship.

    Check for existence of a ship on board at passed in coordinates.
    If there is return an error message and a False value.
    """
    if ship_exists(ship_name, board, ship_length,
                   coordinates, orientation):
        functions.clear_screen()
        player_board.display()
        print('\nSorry, {} cannot be placed,'
              'you already have a ship there,'
              'please choose another location'.format(ship_name))
        return True
    else:
        return False


def out_of_bounds(player_board, ship_length, coordinates, orientation):
    """Check if ship is outside of game board."""
    if orientation == 'v':
        if (ship_length + int(coordinates[1:]) - 1) > constants.BOARD_SIZE:
            functions.clear_screen()
            player_board.display()
            print('\nThat ship exceeds the board size.'
                  'Please choose another location or orientation')
            return True
        else:
            return False

    if orientation == 'h':
        if (ship_length + constants.VALID_LETTERS.index(coordinates[0])) > \
                constants.BOARD_SIZE:
            functions.clear_screen()
            print('\nThat ship exceeds the board size.'
                  'Please choose another location or orientation')
            return True
        else:
            return False
