"""Module encapsulating all Board vars, classes and functions."""

import constants


class Board:
    """Class that defines a the Board object for the game."""

    def __init__(self):
        """Class initialization method instantiating empty board var."""
        self.board = constants.EMPTY_BOARD

    def get_board(self):
        """Method allowing for retrieval of raw board list."""
        return self.board

    def update_board(self, ship_name, ship_length, orientation, position):
        """Class method allowing for updating of players board."""
        column = constants.VALID_LETTERS.index(position[0])
        row = int(position[1]) - 1

        print(column, row)
        if orientation.lower() == 'h':
            # if HORIZONTAL_SHIP and VERTICAL_SHIP not in \
            #         self.board[row][column:(column + ship_length)]:
            self.board[row][column:(column + ship_length)] = \
                ['-' for num in range(ship_length)]
            # else:
            #     print('Sorry, {} cannot be placed, '
            #           'you already have a ship there,'
            #           ' please choose another location'.format(ship_name))
        if orientation.lower() == 'v':
            # v_pos = list()
            # for board_row in range(row, (row + ship_length)):
            #     v_pos.append(self.board[board_row][column])
            #
            # if HORIZONTAL_SHIP and VERTICAL_SHIP not in v_pos:
            for board_row in range(row, (row + ship_length)):
                self.board[board_row][column] = '|'
            # else:
            #     print('Sorry, {} cannot be placed, '
            #           'you already have a ship there,'
            #           ' please choose another location'.format(ship_name))

        return self.board

    def print_board(self, board=constants.EMPTY_BOARD):
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
