class Option():
    '''
    A class for an otion the player gets to makes
    '''
    pass

class Choice():
    '''
    A class for player's making choices
    '''
    def __init__(self, options, min_chosen=1, max_chosen=1):
        self.options = options
        self.min_chosen = min_chosen
        self.max_chosen = max_chosen