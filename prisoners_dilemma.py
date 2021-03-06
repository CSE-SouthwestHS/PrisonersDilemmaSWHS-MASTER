"""
An iterated prisoner's dilemma written by Arthur Goldman
for Southwest High School in Minneapolis's Computer Science class 2016-2017
arthur@goldman-tribe.org
agol1801@mpsedu.org
"""

import GLOBALS
from teamclass import Team
from pandas import DataFrame
import random
from typing import List

default_module_names = ['examplemodules/example0.py',
                        'examplemodules/example1.py',
                        'examplemodules/example2.py',
                        'examplemodules/example3.py']


def load_modules(module_names: List[str]):
    """
    Given a list of strings with paths to modules,
    load them. Return a list of teams, which are
    instances of Team from teamclass.py
    """
    teams = [Team(module_name, team_number) for team_number, module_name in enumerate(module_names)]
    return teams


def play_tournament(modules: List[Team], suppress_exceptions: bool = False, step_rounds: bool = False):
    scores = [[None for _ in range(len(modules))] for _ in range(len(modules))]  # an n*n list for scores
    # each player's scores are in scores[that_player][opponent]
    moves = [[None for _ in range(len(modules))] for _ in range(len(modules))]  # an n*n list for moves
    for first_team_index in range(len(modules)):
        for second_team_index in range(first_team_index + 1):
            # each player plays against all the players before them
            if first_team_index == second_team_index:
                # if you're playing yourself, score 0 and make no moves
                scores[first_team_index][first_team_index] = 0
                moves[first_team_index][first_team_index] = ''
            else:
                # play against the opponent, log scores in the lists
                player_1 = modules[first_team_index]
                player_2 = modules[second_team_index]
                if step_rounds:
                    make_section_title(f"{player_1.team_name} vs. {player_2.team_name}")
                    input()
                player_1_score, player_2_score, player_1_moves, player_2_moves = play_round(player_1, player_2, suppress_exceptions)
                scores[first_team_index][second_team_index] = player_1_score
                scores[second_team_index][first_team_index] = player_2_score
                moves[first_team_index][second_team_index] = player_1_moves
                moves[second_team_index][first_team_index] = player_2_moves
                if step_rounds:
                    print(f"{player_1.team_name} scored {player_1_score} points")
                    print(f"{player_2.team_name} scored {player_2_score} points")
                    if player_1_score > player_2_score:
                        print(f"{player_1.team_name} won against {player_2.team_name}!")
                    elif player_1_score < player_2_score:
                        print(f"{player_2.team_name} won against {player_1.team_name}!")
                    else:
                        print(f"{player_1.team_name} and {player_2.team_name} have tied!")
                    input()
                    display_standings(modules, scores)
                    input()
    return scores, moves


def play_round(player_1: Team, player_2: Team, suppress_exceptions: bool = True):
    number_of_rounds = random.randint(100, 200)  # Plays a random number of rounds between 100 and 200
    player_1_moves = ''  # we store moves as a string of 'b's and 'c's with crashes being an 'n'
    player_2_moves = ''
    player_1_score = 0
    player_2_score = 0
    player_1_crashes = 0
    player_2_crashes = 0
    for _ in range(number_of_rounds):
        player_1_single_score, \
            player_2_single_score, \
            player_1_single_move, \
            player_2_single_move \
            = play_single_dilemma(player_1,
                                  player_2,
                                  player_1_score,
                                  player_2_score,
                                  player_1_moves,
                                  player_2_moves,
                                  suppress_exceptions)
        player_1_score += player_1_single_score
        player_2_score += player_2_single_score
        player_1_moves += player_1_single_move
        player_2_moves += player_2_single_move
        if player_1_single_move == 'n':
            player_1_crashes += 1
        if player_2_crashes == 'n':
            player_2_crashes += 1
    player_1_score = int(player_1_score / number_of_rounds)
    player_2_score = int(player_2_score / number_of_rounds)
    # Take the integer average score for each player so that it doesn't matter that we're doing a random number of rounds
    if player_1_crashes > 0:
        print(f"{player_1.team_name} crashed in {player_1_crashes} matches against {player_2.team_name}")
    if player_2_crashes > 0:
        print(f"{player_2.team_name} crashed in {player_2_crashes} matches against {player_1.team_name}")
    return player_1_score, player_2_score, player_1_moves, player_2_moves


def play_single_dilemma(player_1: Team,
                        player_2: Team,
                        player_1_score: int,
                        player_2_score: int,
                        player_1_moves: str,
                        player_2_moves: str,
                        suppress_exceptions: bool = True):
    player_1_round_score = 0
    player_2_round_score = 0

    try:
        player_1_move = player_1.move(player_1_moves,
                                      player_2_moves,
                                      player_1_score,
                                      player_2_score,
                                      player_2.team_name)
    except Exception:
        player_1_move = 'n'
        if not suppress_exceptions:
            raise

    try:
        player_2_move = player_2.move(player_2_moves,
                                      player_1_moves,
                                      player_2_score,
                                      player_1_score,
                                      player_1.team_name)
    except Exception:
        player_2_move = 'n'
        if not suppress_exceptions:
            raise

    if player_1_move not in GLOBALS.ACCEPTABLE_RESPONSES:
        player_1_round_score = GLOBALS.CRASH
        player_1_move = 'n'
    elif player_2_move not in GLOBALS.ACCEPTABLE_RESPONSES:
        player_2_round_score = GLOBALS.CRASH
        player_2_move = 'n'
    elif (player_1_move == GLOBALS.COLLUDE) and (player_2_move == GLOBALS.COLLUDE):
        player_1_round_score += GLOBALS.REWARD
        player_2_round_score += GLOBALS.REWARD
    elif (player_1_move == GLOBALS.COLLUDE) and (player_2_move == GLOBALS.BETRAY):
        player_1_round_score += GLOBALS.SUCKER
        player_2_round_score += GLOBALS.TEMPTATION
    elif (player_1_move == GLOBALS.BETRAY) and (player_2_move == GLOBALS.COLLUDE):
        player_1_round_score += GLOBALS.TEMPTATION
        player_2_round_score += GLOBALS.SUCKER
    elif (player_1_move == GLOBALS.BETRAY) and (player_2_move == GLOBALS.BETRAY):
        player_1_round_score += GLOBALS.PUNISHMENT
        player_2_round_score += GLOBALS.PUNISHMENT
    return player_1_round_score,\
        player_2_round_score,\
        player_1_move,\
        player_2_move,


def make_section_title(title: str):
    print('{:-^80}'.format(''))
    print('{:^80}'.format(title))
    print('{:-^80}'.format(''))


def display_team_info(team: Team):
    print(f'P{team.team_number}: {team.team_name} using {team.strategy_name} ({team.strategy_description})')


def display_lineup(teams: List[Team]):
    make_section_title('Lineup')
    for team in teams:
        display_team_info(team)


def display_pvp_score(scores: List[List[int]]):
    make_section_title('Player vs. Player Scores')
    print("To find player n's average score against player m, check the nth row and the mth column")
    print(DataFrame(scores))


def display_standings(teams: List[Team], scores: List[List[int]]):
    make_section_title('Standings')
    for team_index in range(len(teams)):
        teams[team_index].summed_scores = sum(filter(None, scores[team_index]))
    teams.sort(key=lambda team: team.summed_scores, reverse=True)
    for team_index in range(len(teams)):
        team = teams[team_index]
        print('{0:2}) {1:<16}(P{2}): {3:>8} points with {4:<20}'.format(team_index + 1, team.team_name, team.team_number, team.summed_scores, team.strategy_name))


def main(module_names: List[str], should_random: bool = False, suppress_exceptions: bool = False, step_rounds: bool = False):
    teams = load_modules(module_names)
    assert len(teams) > 1, "You must supply 1 or more valid team modules"
    if should_random:
        random.shuffle(teams)
    display_lineup(teams)
    if step_rounds:
        input()
    scores, moves = play_tournament(teams, suppress_exceptions, step_rounds)
    display_pvp_score(scores)
    display_standings(teams, scores)
