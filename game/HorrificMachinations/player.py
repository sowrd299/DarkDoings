from card import Card
from deck import Deck

class Player():
    '''
    a class to repressent an player object in-game
    '''

    def __init__(self, deck : Deck):
        # major attributes
        self.deck = deck
        # card zones
        self._hand = []
        self._schemes = []
        self._assets = []
        self._party = []
        self._resources = []

    def start_turn(self):
        '''
        to be called at the start of turn
        '''
        pass

    # STUDY 

    def _draw_to(self, card : Card, zone : list)
        self.deck.remove(card)
        zone.append(card)

    def draw_to_hand(self, card):
        self._draw_to(card, self._hand)

    def draw_to_resource(self, card):
        self._draw_to(card, self._resources)

    # INVESTIGATE

    def set_party(self, party : [Asset]):
        '''
        Set's the player's current party for investigating
        WILL let you add assets to your party that you do not own
        '''
        self._party = party

    # GET INFORMATION

    def get_resources(self):
        '''
        returns how many resources the player has
        '''
        return len(resources)