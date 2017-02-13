"""Module that contains all Player classes, vars and functions."""

from board import Board
import constants
import functions
import validation


class Player(object):
    """Define the player class."""

    def place_ships(self, ships):
        """Place user ships on board object.

        This method allowing players to run through a list of ships
        passed in and place each one simultaneously updating the players board.
        """
        for ship_name, ship_length in ships:

            while True:
                coordinates = functions \
                    .get_ship_coordinates(ship_name, ship_length, self.name)

                orientation = functions.get_ship_orientation()

                ship = {
                    "orientation":  orientation,
                    "coordinates": coordinates,
                    "ship_length": ship_length
                    }

                if validation.collision(ship_name,
                                        self.board.get_board(), **ship):
                    continue

                if validation.out_of_bounds(**ship):
                    continue

                break  # if we get here ship placement is valid so break out.

            self.board.update_board(**ship)

            functions.clear_screen()
            self.board.display()

        input('{}, your ships have been placed!'
              ' Press Enter to continue.'.format(self.name))

    def get_shot(self):
        """Ask player to pick a location to shoot at."""
        shot = input("{}, enter a target location"
                     " on your opponents board: ".format(self.name))

        if validation.are_valid_coordinates(shot):
            if validation.is_valid_shot(shot, self.shot_list):
                self.shot_list.append(shot)
                return shot
            else:
                print("You've already shot at that location. Please enter a new target location\n")
                return self.get_shot()
        else:
            return self.get_shot()

    def shoot(self, other_player, board):
        """Player method for guessing location of enemy ships."""
        functions.clear_screen()
        self.shots_board.display()
        self.board.display()

        coordinates = self.get_shot()

        column = constants.VALID_LETTERS.index(coordinates[0])
        row = int(coordinates[1:]) - 1

        if validation.are_valid_coordinates(coordinates):
            if validation.hit_or_miss(coordinates, board):
                board[row][column] = constants.HIT
                self.shots_board.get_board()[row][column] = constants.HIT
            else:
                board[row][column] = constants.MISS
                self.shots_board.get_board()[row][column] = constants.MISS

        input('Please pass the game to {}, and look away.\nPress Enter to continue'.format(other_player))

    def turn(self, other_player, shooting=False):
        """Method to describe logic governing each player's turn."""
        if not shooting:
            functions.clear_screen()

            input('{} prepare to place your fleet.'
                  ' Please have {} look away and press Enter to begin.'
                  .format(self.name, other_player))

            self.board.display()
            self.place_ships(constants.SHIP_INFO)
        else:
            self.shoot()

    def __init__(self, player='Player One'):
        """Override class __init__ method."""
        self.name = input("{}, Please enter your name:"
                          .format(player)).capitalize()
        self.board = Board()
        self.shots_board = Board()
        self.shot_list = list()
