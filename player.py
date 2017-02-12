"""Module that contains all Player classes, vars and functions."""

import functions
import validation


class Player(object):
    """Define the player class."""

    def get_ship_coordinates(self, ship_name, ship_length):
        """Ask input from user on where to put each ship."""
        prompt = "{}, Choose a position for the {} ({} spaces):"
        ship_coordinates = input(prompt.format(
            self.name, ship_name, ship_length))

        if validation.are_valid_coordinates(ship_coordinates, ship_length):
            return ship_coordinates
        else:
            return self.get_ship_coordinates(ship_name, ship_length)

    def get_ship_orientation(self):
        """Method to get ship orientation input from player."""
        ship_orientation = input("{}, Please choose an orientation"
                                 " [V]ertical or [H]orizontal): "
                                 .format(self.name)).lower()

        if validation.is_valid_orientation(ship_orientation):
            return ship_orientation
        else:
            return self.get_ship_orientation()

    def place_ships(self, ships, board):
        """Place user ships on board object.

        This method allowing players to run through a list of ships
        passed in and place each one simultaneously updating the players board.
        """
        functions.clear_screen()

        for ship_name, ship_length in ships:
            while True:

                coordinates = self.get_ship_coordinates(ship_name, ship_length)
                orientation = self.get_ship_orientation()

                if validation.collision(ship_name, ship_length,
                                        coordinates, orientation, board):
                    continue

                if validation.out_of_bounds(ship_length, coordinates,
                                            orientation):
                    continue

                break

            ship_data = {
                "orientation":  orientation,
                "position": coordinates,
                "ship_name": ship_name,
                "ship_length": ship_length
                }

            functions.clear_screen()

            board.print_board(board.update_board(**ship_data))

    def __init__(self, player='Player One', **kwargs):
        """Override class __init__ method."""
        self.name = input("{}, Please enter your name:"
                          .format(player)).capitalize()
