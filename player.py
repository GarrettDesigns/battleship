from board import Board

class Player:

    def get_name(self):
        self.name = input("What is your name?: ")
        return self.name

    def place_ships(self, ships):
        for ship_name, ship_length in ships:
            ship_position = input("Choose a location for the {}: ".format(ship_name))
            ship_orientation = input("Please choose an orientation ([V]ertical or [H]orizontal): ")
            return ship_position, ship_orientation
