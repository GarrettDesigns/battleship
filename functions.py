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
    print("   " + " ".join(constants.BOARD_HEADING))

    row_num = 1
    for row in board:
        print(str(row_num).rjust(2) + " " + (" ".join(row)))
        row_num += 1


def get_ship_coordinates(ship_name, ship_length, player_name):
    """Ask input from user on where to put each ship."""
    prompt = "{}, Choose a position for the {} ({} spaces):"
    ship_coordinates = input(prompt
                             .format(player_name, ship_name, ship_length))

    if validation.are_valid_coordinates(ship_coordinates):
        return ship_coordinates
    else:
        return get_ship_coordinates(ship_name, ship_length, player_name)


def get_ship_orientation():
    """Method to get ship orientation input from player."""
    ship_orientation = input("Please choose an orientation"
                             " [V]ertical or [H]orizontal): ")

    if validation.is_valid_orientation(ship_orientation):
        return ship_orientation
    else:
        return get_ship_orientation()
