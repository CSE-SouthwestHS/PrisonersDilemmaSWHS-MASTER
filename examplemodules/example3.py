####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import GLOBALS

team_name = 'E3'
strategy_name = 'Collude but retaliate'
strategy_description = """\
Collude first round. Collude, except in a round after getting 
a severe punishment."""


def move(my_history, their_history, my_score, their_score, opponent_name):
    """Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Note:  Instead of hard coding 'c' or 'b', this function refers to the GLOBAL variables.
    Some would consider this a more elegant way to reference these values since if the value for
    colluding or betraying were to change, changing those in the GLOBALS module would propagate.
    The next example module accomplishes this more efficiently.
    """
    if len(my_history) == 0:  # It's the first round; collude.
        return GLOBALS.COLLUDE
    elif my_history[-1] == GLOBALS.COLLUDE and their_history[-1] == GLOBALS.BETRAY:
        return GLOBALS.BETRAY  # Betray if they were severely punished last time,
    else:
        return GLOBALS.COLLUDE  # otherwise collude.
