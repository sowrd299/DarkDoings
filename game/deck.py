from card import Card

class Deck():

    def __init__(self):
        self._cards = []

    def populate(cards):
        self._cards = cards

    def get_top_cards(self, number : int):
        return self._cards[0:number]

    def remove(self, card : Card):
        self._cards.remove(card)