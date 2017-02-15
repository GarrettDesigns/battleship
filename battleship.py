"""Module that executes the Battleship Game."""

import functions
from player import Player
import validation


class Battleship(object):
    """Battleship main game class definition."""

    def play_battleship(self):
        """Method to start main battleship game.

        Calling this method initializes players taking turns.

        If a player has no ships left they are sunk and the game ends with
        both boards displayed and the other player being declared the winner
        """
        # Loop over player turns until somebody satisfies the win condition
        while True:
            if validation.player_sunk(self.player_one, self.player_two):
                self.player_one.board.display()
                self.player_two.board.display()
                break

            # Prompt players to choose target locations turn by turn
            self.player_one.shoot(self.player_two)
            self.player_two.shoot(self.player_one)

            test_win_condition = input('Would you like to sink Player One?').lower()

            if test_win_condition == 'y':
                self.player_one.ships_list = []

    def __init__(self):
        """Class initialization method.

        Set up Battleship players and game boards.
        """
        # Clear screen on game initialization
        functions.clear_screen()

        # Instatiate players
        self.player_one = Player()
        self.player_two = Player("Player Two")

        # Prompt players to take turns setting up their boards
        self.player_one.set_up_board(self.player_two.name)
        self.player_two.set_up_board(self.player_one.name)

        # Clear the screen and prepare the first player  \
        # to make targeting choices
        functions.clear_screen()
        play_game = input('\nWould you like to start Battleship? Y/n').lower()

        input('Please pass the board to {}, and look away.\n'
              'Press Enter to continue.'.format(self.player_one.name))

        if play_game != 'n':
            # Initiate the game loop
            self.play_battleship()


# Make sure script can't be executed when imported
if __name__ == '__main__':
    Battleship()
