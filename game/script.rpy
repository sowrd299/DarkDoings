# The script of the game goes in this file.

init python:

    from gameManager import GameManager

    # variables
    players = []
    player_managers = [] # TODO: setup player managers
    gm = GameManager(players)

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("The Voice in Side Your Head")


# The game starts here.
label start:

    v "So here we begin...."
    v "{i} MUA HA HA HA HA {/i}"

    menu:

        "Let's play":
            jump start_turn

    return

# GAME LOGIC
label start_turn:

    python:
        # decide the active player
        active_player_ind = gm.get_active_player_ind()
        active_player = player_managers[active_player_ind]
        # choice type of turn
        turn_options = start_turn(active_player_ind)

    v "What shall we do with our turn...?"