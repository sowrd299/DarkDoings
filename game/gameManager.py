from player import Player
from playerManager import PlayerManager
from card import Card
from choice import Choice
import choice

class GameManager():
    '''
    A class to be home to the root of the gamestate
    and manage game progression
    '''

    # BASIC TURN OPTIONS
    class TurnOption(choice.Option):
        def __init__(self, get_choices, trappable):
            self.get_choices = get_choices
            self.trappable = trappable

    # HOUSE KEEPING and BASIC OPERATIONS
    def __init__(self, players : [Player]):
        '''
        :param players: the players in the game
        '''
        self._players = players
        self._active_player = 0 # the index of the active player

        # setup turn otions
        STUDY_TURN = TurnOption(self.get_draw_options, False) # draw cards and gain resources
        PLAN_TURN = TurnOption(None, False) # play a card
        INVESTIGATE_TURN = TurnOption(None, True) # investigate a scheme
        MOTION_TURN = TurnOption(None, True) # set schemes in motion

    # TURN ADVANCEMENT FUNCTIONS
    def start_turn(self, player_ind : int):
        '''
        runs the next turn of the game
        assumes it is _active_player's turn
        returns options that they can do with their turn
        :param player_ind: the index of the player taking the turn
        '''
        # SETUP VARS
        # assert player_ind == , "It is not "+str(players[player_ind][0])+"'s turn." # this might be too bossy
        player = self._players[player_ind]
        aplayer = self._players[self._active_player]
        # START TURN
        player.start_turn()
        # Return the options for what to do with a turn
        return Choice([self.STUDY_TURN, self.PLAN_TURN, self.INVESTIGATE_TURN, self.MOTION_TURN])

    def set_turn_option(self, player_ind : int, option : TurnOption) -> [Choice]:
        '''
        Set the kind of turn we are currently in
        The second thing to be called every turn
        '''
        self._current_turn = option

        return option.get_choices(self._players[player_ind])

    # STUDY

    def get_draw_options(self, player):
        '''
        Of the options returned, one is to be added to hand
        the other becomes a resource
        '''
        return Choice(player.deck.get_top_cards(2)) 

    def set_draw(self, player_ind, card : Card, choice : Choice):
        # draw the chosen card
        self._players[player_ind].draw_to_hand(card)
        # make the remaining cards resources
        for c in choice.options:
            if c != card:
                self._players[player_ind].draw_to_resource(c)

    # OTHER MANAGEMENT FUNCTIONS
    def game_ongoing(self):
        '''
        returns if the game is still ongoing
        or if it has endeded
        '''
        return True

    def next_turn(self):
        '''
        progresses to the next turn of the game
        '''
        self._active_player += 1
        self._active_player %= len(self._players)

    def get_active_player_ind(self):
        '''
        returns the index of the current active player
        '''
        return self._active_player