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

    def start_turn(self, player, option):
        '''
        runs the next turn of the game
        assumes it is _active_player's turn
        '''
        # SETUP VARS
        aplayer, aplayer_manager = self._players[self._active_player]
        assert player == aplayer, "It is not "+str(player)+"'s turn." # this might be too bossy
        # START TURN
        aplayer.start_turn()
        aplayer_manager.start_turn()
        # 

    def next_turn(self):
        '''
        progresses to the next turn of the game
        '''
        self._active_player += 1
        self._active_player %= len(self._players)