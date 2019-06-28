"""Module containing methods for performing player input validation."""

from constants import (
    HORIZONTAL_SHIP, VERTICAL_SHIP, VALID_LETTERS, BOARD_HEADING, BOARD_SIZE)
from functions import (
    clear_screen,
    clear_screen_and_print_message,
    clear_screen_and_print_result
)

def is_ship_in_location(location):
    if HORIZONTAL_SHIP in location \
      or VERTICAL_SHIP in location:
        return True

    return False

def ship_exists(ship_name, board, ship_length, coordinates, orientation):
    """Check if a ship already occupies position of player input."""
    column = VALID_LETTERS.index(coordinates[0])
    row = int(coordinates[1:]) - 1

    if orientation.lower() == 'h':
        chosen_location = board[row][column:(column + ship_length)]
        return is_ship_in_location(chosen_location)


    if orientation.lower() == 'v':
        v_pos = list()

        try:
            for row in range(row, (row + ship_length)):
                v_pos.append(board[row][column])
        except IndexError:
            return None

        return is_ship_in_location(v_pos)


def hit_or_miss(coordinates, board):
    """Check whether player shot is a hit or miss."""
    coordinates = coordinates.strip()

    column = VALID_LETTERS.index(coordinates[0])
    row = int(coordinates[1:]) - 1
    board_position = board[row][column]
    print(board_position)
    if  board_position == '-' or board_position == '|':
        clear_screen_and_print_result('HIT', True)

    clear_screen_and_print_result('MISS', False)


def is_valid_shot(shot, shot_list):
    """Define logic to ensure the player doesn't shoot the same spot twice."""
    if shot not in shot_list:
        return True

    clear_screen()
    return False


def are_valid_coordinates(coords, player_board, shots_board):
    """Check if ship coordinates are valid."""
    message = ''
    is_valid = True
    column = coords[0]

    if len(coords) > 3:
        message = '\n{} is not a valid entry. ' \
            'Please enter a column ({}-{}) and a row (1-{}), ex. "h4"' \
            .format(coords, BOARD_HEADING[0],
                BOARD_HEADING[(BOARD_SIZE - 1)], BOARD_SIZE)
        is_valid = False

    if len(coords) < 2 or coords == '':
        message = '\nYou must enter at least one column (letter) ' \
              'and one row (number), ex. "b8"'
        is_valid = False

    try:
        row = int(coords[1:])
    except ValueError:
        message = '\n{} is not a valid row, valid rows are numbered 1-{}' \
            .format(row, BOARD_SIZE)
        is_valid = False

    if column not in VALID_LETTERS:
        message = "\n{} is not a valid column valid lettered columns are {}" \
              .format(column, VALID_LETTERS)
        is_valid = False

    if row > BOARD_SIZE:
        message = '\n{} is not a valid row, valid rows are numbered 1-{}' \
              .format(row, BOARD_SIZE)
        is_valid = False

    clear_screen_and_print_message(player_board, message, shots_board)
    return is_valid


def is_valid_orientation(orientation, player_board):
    """Check for valid orientation input."""
    message = '\n{} is not a valid orientation,' \
        ' please enter either "h" or "v"'.format(orientation)

    if orientation not in 'hv' or orientation == '':
        clear_screen_and_print_message(player_board, message)
        return False

    return True


def player_sunk(player):
    """Detect if either player has lost all of their ships."""
    if not player.ships_list:
        print('**************\n*** WINNER ***\n**************')
        print("{} sunk their opponent!"
              .format(player.name))
        return True

    return False

def collision(player_board, ship_name, board, ship_length,
              coordinates, orientation):
    """Check if ship collides with another ship.

    Check for existence of a ship on board at passed in coordinates.
    If there is return an error message and a False value.
    """
    message = '\nSorry, {} cannot be placed, ' \
              'you already have a ship there.'.format(ship_name)

    if ship_exists(ship_name, board, ship_length, coordinates, orientation):
        clear_screen_and_print_message(player_board, message)
        return True

    return False

def does_ship_fit_board(board, selected_location):
    message = '\nThat ship exceeds the board size.' \
              ' Please choose another location or orientation'

    if selected_location > BOARD_SIZE:
        clear_screen_and_print_message(board, message)
        return True

    return False

def out_of_bounds(player_board, ship_length, coordinates, orientation):
    """Check if ship is outside of game board."""
    if orientation == 'v':
        ship_length_plus_location = (ship_length + int(coordinates[1:]) - 1)

    if orientation == 'h':
        ship_length_plus_location = (
          ship_length + VALID_LETTERS.index(coordinates[0]))

    return does_ship_fit_board(player_board, ship_length_plus_location)
