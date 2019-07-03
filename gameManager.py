from player import Player
from playerManager import PlayerManager

class GameManager():
    '''
    A class to be home to the root of the gamestate
    and manage game progression
    '''

    def __init__(self, players : [(Player, PlayerManager)]):
        '''
        :param players: the players in the game
        '''
        self._players = players
        self._active_player = 0 # the index of the active player

    def run_turn(self):
        '''
        runs the next turn of the game
        assumes it is _active_player's turn
        '''
        # SETUP VARS
        player, player_manager = self._players[self._active_player]
        # START TURN
        player.start_turn()
        player_manager.start_turn()
        # FIGURE OUT WHAT THE PLAYER IS DOING WITH THEIR TURN
        turn_action = player.get_turn_choice()

    def next_turn(self):
        '''
        progresses to the next turn of the game
        '''
        self._active_player += 1
        self._active_player %= len(self._players)