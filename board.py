class Board:

    BOARD_SIZE = 10
    BOARD_HEADING = [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'

    def create_board(self, marker):
        board = [[marker for space in range(self.BOARD_SIZE)] for row in range(self.BOARD_SIZE)]
        return board

    def update_board(self, board, ship_placement):
        current_board = list(board)
        ship_coordinates, ship_orientation = ship_placement
        ship_column, ship_row = tuple(ship_coordinates)

        print('Ship Column: {}, Ship Row: {}, Ship Orientation: {}'.format(ship_column, ship_row,  ship_orientation.lower()))

        for row in current_board:
            print(row)

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
