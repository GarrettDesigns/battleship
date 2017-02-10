"""Module containing constants for use in other modules."""

SHIP_INFO = [
    ("Aircraft Carrier", 5),
    ("Battleship", 4),
    ("Submarine", 3),
    ("Cruiser", 3),
    ("Patrol Boat", 2)
]

MISS = '.'
HIT = '*'
SUNK = '#'

EMPTY = '0'
BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'

BOARD_HEADING = [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]
EMPTY_BOARD = [[EMPTY for space in range(BOARD_SIZE)]
               for row in range(BOARD_SIZE)]

VALID_LETTERS = ''.join(BOARD_HEADING).lower()
