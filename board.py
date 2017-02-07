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

def place_ship(self, location, orientation, board, ship_info):
    ship_name, ship_length = ship_info
    alpha = ''.join(self.BOARD_HEADING).lower()
    column, row = location

    row = row - 1
    column = alpha.index(column)

    if orientation.lower() == 'h':
        if self.HORIZONTAL_SHIP not in board[row][column:(column + ship_length)] and self.VERTICAL_SHIP not in board[row][column:(column + length)]:
            board[row][column:(column + ship_length)] = ['-' for num in range(ship_length)]
        else:
            print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship))

    if orientation.lower() == 'v':
        v_pos = list()

        for board_row in range(row, (row + ship_length)):
            v_pos.append(board[board_row][column])

        if self.HORIZONTAL_SHIP not in v_pos and self.VERTICAL_SHIP not in v_pos:
            for board_row in range(row,(row + ship_length)):
                board[board_row][column] = '|'
        else:
            print('Sorry, {} cannot be placed, you already have a ship there, please replace your ship'.format(ship))

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
