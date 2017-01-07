from board import Board

class Player:

    def get_name(self):
        self.name = input("What is your name?: ")
        return self.name

    def place_ships(self, ships):
        player_ships = {}
        for ship_name, ship_length in ships:
            ship_position = input("Choose a location for the {}: ".format(ship_name))
            ship_orientation = input("Please choose an orientation ([V]ertical or [H]orizontal): ")
            player_ships[ship_name] = {"orientation":  ship_orientation, "position": tuple(ship_position), "length": ship_length}
        return player_ships
