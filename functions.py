"""Module with utility functions."""

import constants
import validation


def clear_screen():
    """Function that provides a clear screen for program."""
    print("\033c", end="")


def print_board(board):
    """Function to print the game board.

    First print three spaces.

    c will take on the value of each number
    specified in range(ord('A'), ord('A') + BOARD_SIZE).
    passing each number to chr(c) generates
    the letter equivalent of that number

    In this case with board_SIZE == 10
    and range(ord('A'), ord('A') + board_SIZE) == range(66, 76)

    This loop will iterate though the numbers 66-76
    By passing each number to chr() via the iterator variable c
    it will print out the letters A-J
    """
    print('\n')
    print("   " + " ".join(constants.BOARD_HEADING))

    for row_num, row in enumerate(board):
        print(str(row_num + 1).rjust(2) + " " + (" ".join(row)))


def get_ship_coordinates(ship_name, ship_length, player_name,
                         player_board, shots_board=''):
    """Ask input from user on where to put each ship.

    This method makes use of the validation module to check
    whether or not coordinates are valid after recieving input.
    """
    prompt = "{}, Choose a position for the {} ({} spaces):"
    ship_coordinates = input(prompt
                             .format(player_name, ship_name,
                                     ship_length)).lower().replace(' ', '')

    if validation.are_valid_coordinates(ship_coordinates,
                                        player_board, shots_board):
        return ship_coordinates
    else:
        return get_ship_coordinates(ship_name, ship_length,
                                    player_name, player_board, shots_board)


def get_ship_orientation(player_board):
    """Method to get ship orientation input from player.

    This method makes use of the validation module to check whether the
    orientation is valid after receiving input.
    """
    ship_orientation = input("Please choose an orientation"
                             " [V]ertical or [H]orizontal): "
                             ).lower().replace(' ', '')

    if validation.is_valid_orientation(ship_orientation, player_board):
        return ship_orientation
    else:
        return get_ship_orientation(player_board)
