from board import Board


class Player:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def place_ships(self, ships):
        for ship_name, ship_length in ships:
            ship_position = input("Choose a location for the {}: ".format(ship_name))
            ship_orientation = input("Please choose an orientation ([V]ertical or [H]orizontal): ").lower()

            ship_data = {"orientation":  ship_orientation, "position": tuple(ship_position), "length": ship_length, "name": ship_name}


            print(Board().print_board(Board().update_board(**ship_data)))
