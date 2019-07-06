'''
NOT IN USE
'''

from gameManager import GameManager
from playerManager import PlayerManager
from choice import Choice

def give_choice(player_manager : PlayerManager, choice : Choice):
    player_manager.answer_choice(choice)

def take_turn(gm : GameManager, player_managers : PlayerManager):
    '''
    play the next turn of the game
    '''
    # decide the active player
    active_player_ind = gm.get_active_player_ind()
    active_player = player_managers[active_player_ind]
    # choice type of turn
    turn_options = start_turn(active_player_ind)
    turn_option = give_choice(active_player, turn_options)
    gm.set_turn_option(active_player_ind, turn_option)
    # more choices!
    for choice in 
    

if __name__ == "__main__":

    # setup vars
    players = []
    player_managers = [] # TODO: setup player managers
    gm = GameManager(players)

    while gm.game_ongoing():
        take_turn(gm, )