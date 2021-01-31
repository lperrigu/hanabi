# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lperrigu <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/06/20 15:13:45 by lperrigu          #+#    #+#              #
#    Updated: 2017/06/20 16:39:19 by lperrigu         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from tools import played

def give_hint(deck, hands, board_state, tokens, current_player):
    if token['hint'] == 0:
        return False
    possible_play = []
    for player_i in len(hands):
        if player_i != current_player:
            for i in range(len(hands[player_i])):
                number = hands[player_i][i][0]
                color = hands[player_i][i][1]
                unknowed = not hands[player_i][i][2] and not hands[player_i][i][3]
                # Compter le nombre de carte hintee
                # privilegier celle avec le max de jouable sans ambiguite
                if board_state[color] == hands


def safe_discard(deck, hands, board_state, tokens, current_player):
    hands[current_player][0][0] = 3
    hands[current_player][0][1] = 'r'
    hands[current_player][0][2] = True
    hands[current_player][0][3] = True
    board_state['r'] = 4
    for i in range(len(hands[current_player])):
        number = hands[current_player][i][0]
        color = hands[current_player][i][1]
        knowed = hands[current_player][i][2] and hands[current_player][i][3]
        if board_state[color] >= number and knowed:
            discarded(i, deck, hands, board_state, tokens, current_player)
            return True
    return False


def play_something(deck, hands, board_state, tokens, current_player):
    print(hands[current_player])
    print(board_state)
    for i in range(len(hands[current_player])):
        number = hands[current_player][i][0]
        color = hands[current_player][i][1]
        knowed = hands[current_player][i][2] and hands[current_player][i][3]
        if board_state[color] == number - 1 and knowed:
            played(i, deck, hands, board_state, tokens, current_player)
            return True
    return False


def play_a_five(deck, hands, board_state, tokens, current_player):
    #hands[current_player][0][0] = 5
    #hands[current_player][0][1] = 'w'
    #hands[current_player][0][2] = True
    #hands[current_player][0][3] = True
    #board_state['w'] = 4
    #print(hands[current_player])
    #print(board_state)
    for i in range(len(hands[current_player])):
        number = hands[current_player][i][0]
        color = hands[current_player][i][1]
        knowed = hands[current_player][i][2] and hands[current_player][i][3]
        if number == 5 and board_state[color] == 4 and knowed:
            played(i, deck, hands, board_state, tokens, current_player)
            return True
    return False


def computer_play(deck, hands, board_state, tokens, current_player):
    if play_a_five(deck, hands, board_state, tokens, current_player):
        return
    if play_something(deck, hands, board_state, tokens, current_player):
        return
    if safe_discard(deck, hands, board_state, tokens, current_player):
        return
    #if give_hint(deck, hands, board_state, tokens, current_player):
    #    return
    #yolo_discard(deck, hands, board_state, tokens, current_player)
