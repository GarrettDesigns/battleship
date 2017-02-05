class Board:

    MISS = '.'
    HIT = '*'
    SUNK = '#'

    EMPTY = 'O'
    BOARD_SIZE = 10
    BOARD_HEADING = [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]
    BOARD = [[EMPTY for space in BOARD_SIZE] for row in BOARD_SIZE]

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'

    def print_board(self, board):
        '''first print three spaces

        c will take on the value of each number
        specified in range(ord('A'), ord('A') + BOARD_SIZE).
        passing each number to chr(c) generates
        the letter equivalent of that number

        In this case with board_SIZE == 10
        and range(ord('A'), ord('A') + board_SIZE) == range(66, 76)

        This loop will iterate though the numbers 66-76
        By passing each number to chr() via the iterator variable c
        it will print out the letters A-J
        '''

        print("   " + " ".join(self.BOARD_HEADING))

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
