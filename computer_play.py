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

#def obvious_play(deck, hands, board_state, tokens, current_player):


def play_a_five(deck, hands, board_state, tokens, current_player):
    


def computer_play(deck, hands, board_state, tokens, current_player):
    #obvious_play(deck, hands, board_state, tokens, current_player)
    if play_a_five(deck, hands, board_state, tokens, current_player):
        return
    if play_something(deck, hands, board_state, tokens, current_player)
        return
    if safe_discard(deck, hands, board_state, tokens, current_player)
        return
    if give_hint(deck, hands, board_state, tokens, current_player)
        return
    yolo_discard(deck, hands, board_state, tokens, current_player)
