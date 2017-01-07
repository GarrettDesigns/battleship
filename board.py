class Board:

    BOARD_SIZE = 10
    BOARD_HEADING = [chr(c) for c in range(ord('A'), ord('A') + BOARD_SIZE)]

    VERTICAL_SHIP = '|'
    HORIZONTAL_SHIP = '-'

    def create_board(self, marker):
        board = [[marker for space in range(self.BOARD_SIZE)] for row in range(self.BOARD_SIZE)]
        return board

    def update_board(self, board, player_ships):
        current_board = list(board)

        for ship_name, position_info in player_ships.items():
            ship_column, ship_row = position_info["position"]
            ship_orientation = position_info["orientation"]
            ship_length = position_info["length"]
            print("ship name: {} -- ship column: {} -- ship orientation: {} -- ship length: {}".format(ship_name, ship_column, ship_orientation, ship_length))

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
