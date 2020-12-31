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
    #obvious_play(deck, hands, board_state, tokens, current_player)
    if play_a_five(deck, hands, board_state, tokens, current_player):
        return
    if play_something(deck, hands, board_state, tokens, current_player):
        return
    if safe_discard(deck, hands, board_state, tokens, current_player):
        return
    if give_hint(deck, hands, board_state, tokens, current_player):
        return
    yolo_discard(deck, hands, board_state, tokens, current_player)
