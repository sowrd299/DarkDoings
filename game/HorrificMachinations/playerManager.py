from choice import Choice
from choice import Option

class PlayerManager():
    '''
    An abstract class to manage IO with a real-world player or AI
    '''

    def start_turn(self):
        '''
        to be called at start of turn
        for IO and the such 
        '''
        pass

    def answer_choice(self, choice : Choice) -> Option:
        '''
        Decides the given choice
        '''
        raise NotImplementedError
