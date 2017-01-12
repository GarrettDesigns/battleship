class Board:

    BOARD_SIZE = 10
    BOARD_HEADING = [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'

    def create_board(self, marker):

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
        heading = "   " + " ".join(self.BOARD_HEADING) + "\n"
        row = [[marker for space in range(self.BOARD_SIZE)] for row in range(self.BOARD_SIZE)]

        board = ''
        board += heading

        row_num = 1
        for row_list in row:
            board += str(row_num).rjust(2) + " " + (" ".join(row_list)) + "\n"
            row_num += 1
        return board

    def update_board(self, board, player_ships):
        current_board = list(board)
        # print(current_board)
        for row_num, row in enumerate(current_board):
            print("row num: {}, row: {}".format(row_num, row))

        for ship_name, position_info in player_ships.items():
            ship_column, ship_row = position_info["position"]
            ship_orientation = position_info["orientation"]
            ship_length = position_info["length"]

            print("ship name: {} -- ship column: {} -- ship row: {} -- ship orientation: {} -- ship length: {}".format(ship_name, self.BOARD_HEADING.index(ship_column.upper()), ship_row, ship_orientation, ship_length))
