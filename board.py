MISS = '.'
HIT = '*'
SUNK = '#'

EMPTY = '0'
BOARD_SIZE = 10

VERTICAL_SHIP = '|'
HORIZONTAL_SHIP = '-'

BOARD_HEADING = [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]
EMPTY_BOARD = [[EMPTY for space in range(BOARD_SIZE)] for row in range(BOARD_SIZE)]

class Board:

    def __init__(self):
        self.board = EMPTY_BOARD

    def update_board(self, name, length, orientation, position):

        alpha = ''.join(BOARD_HEADING).lower()

        ship_name = name
        orientation = orientation
        ship_length = length

        column, row = position

        column = alpha.index(column)
        row = int(row) - 1

        if orientation.lower() == 'h':
            if HORIZONTAL_SHIP not in self.board[row][column:(column + ship_length)] and VERTICAL_SHIP not in self.board[row][column:(column + ship_length)]:
                self.board[row][column:(column + ship_length)] = ['-' for num in range(ship_length)]
            else:
                print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship_name))

        if orientation.lower() == 'v':
            v_pos = list()

            for board_row in range(row, (row + ship_length)):
                v_pos.append(self.board[board_row][column])

            if HORIZONTAL_SHIP not in v_pos and VERTICAL_SHIP not in v_pos:
                for board_row in range(row,(row + ship_length)):
                    self.board[board_row][column] = '|'
            else:
                print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship_name))

        return self.board

    def print_board(self, board=EMPTY_BOARD):
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

        print("   " + " ".join(BOARD_HEADING))

        row_num = 1
        for row in board:
            print(str(row_num).rjust(2) + " " + (" ".join(row)))
            row_num += 1
