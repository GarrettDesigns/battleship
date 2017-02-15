"""Module that contains all Player classes, vars and functions."""

from board import Board
import constants
import functions
import validation


class Player(object):
    """Define the player class."""

    def add_to_ship_list(self, orientation, coordinates, ship_length):
        """Add player ships to list of ships on board.

        Get column number via the index of VALID_LETTERS
        which are equal to the string 'abcefghij'

        If ship is horizontal add ship coordinates by
        incrementing the column value which is a letter

        If ship is vertical add ship incrementing the row
        value which is an integer
        """
        column = constants.VALID_LETTERS.index(coordinates[0])

        if orientation == 'h':
            row = coordinates[1:]
            columns = constants.VALID_LETTERS[column:(column + ship_length)]

            for column in columns:
                self.ships_list \
                    .append(constants.VALID_LETTERS[constants.VALID_LETTERS
                            .index(column)] + row)

        if orientation == 'v':
            row = int(coordinates[1:])
            rows = list(range(row, row + ship_length))

            for row in rows:
                self.ships_list \
                    .append(constants.VALID_LETTERS[column] + str(row))

    def place_ships(self, ships):
        """Place user ships on board object.

        This method allowing players to run through a list of ships
        passed in and place each one simultaneously updating the players board.

        For all ships in constants.SHIP_INFO as user for coordinates and
        orientation and feed that info to the board's update method to place
        the ship on the players board.
        """
        for ship_name, ship_length in ships:

            while True:
                coordinates = functions \
                    .get_ship_coordinates(ship_name, ship_length,
                                          self.name, self.board)

                orientation = functions.get_ship_orientation(self.board)

                ship = {
                    "orientation":  orientation,
                    "coordinates": coordinates,
                    "ship_length": ship_length
                    }

                if validation.collision(self.board, ship_name,
                                        self.board.get_board(), **ship):
                    continue

                if validation.out_of_bounds(self.board, **ship):
                    continue

                break  # if we get here ship placement is valid so break out.

            self.add_to_ship_list(orientation, coordinates, ship_length)
            self.board.update_board(**ship)

            functions.clear_screen()
            self.board.display()

        input('{}, your ships have been placed!\n'
              'Press Enter to continue.'.format(self.name))

    def get_shot(self):
        """Ask player to pick a location to shoot at.

        Validate the shot coordinates and that the player has not
        shot at that location previously, if those conditions are met
        then return the shot.
        """
        shot = input("{}, enter a target location"
                     " on your opponents board: "
                     .format(self.name)).lower().replace(' ', '')

        if validation.are_valid_coordinates(shot, self.board,
                                            self.shots_board):
            if validation.is_valid_shot(shot, self.shot_list):
                self.shot_list.append(shot)
                return shot
            else:
                self.shots_board.display()
                self.board.display()
                print("\nYou've already shot at that location."
                      " Please try again.")
                return self.get_shot()
        else:
            return self.get_shot()

    def shoot(self, other_player):
        """Player method for guessing location of enemy ships.

        Validate coordinates and whether the players shot has hit a ship
        and update the players boards accordingly.
        """
        board = other_player.board.get_board()

        functions.clear_screen()
        self.shots_board.display()
        self.board.display()

        coordinates = self.get_shot()

        column = constants.VALID_LETTERS.index(coordinates[0])
        row = int(coordinates[1:]) - 1

        if validation.are_valid_coordinates(coordinates, self.board,
                                            shots_board=self.shots_board):
            if validation.hit_or_miss(coordinates, board):
                board[row][column] = constants.HIT
                self.shots_board.get_board()[row][column] = constants.HIT
                other_player.ships_list.remove(str(coordinates))
            else:
                board[row][column] = constants.MISS
                self.shots_board.get_board()[row][column] = constants.MISS

        input('Please pass the game to {}, and look away.'
              '\nPress Enter to continue'.format(other_player.name))

    def set_up_board(self, other_player):
        """Method to describe logic governing each player's turn."""
        functions.clear_screen()
        input('Please pass the Board to {}.'
              ' Press Enter to continue'.format(self.name))

        functions.clear_screen()
        input('{} prepare to place your fleet.'
              ' Please have {} look away and press Enter to begin.'
              .format(self.name, other_player))

        self.board.display()
        self.place_ships(constants.SHIP_INFO)

    def __init__(self, player='Player One'):
        """Instantiate name, boards, and lists for player.

        This sets up some default attributes for the player, such as
        a board to place ships on and a board to place shots on, as well
        as the players name and a list of the placement of their ships to
        keep track of whether their fleet has been sunk via another method.
        """
        self.name = input("{}, Please enter your first name:"
                          .format(player)).capitalize()
        self.board = Board()
        self.shots_board = Board()
        self.shot_list = list()
        self.ships_list = list()
