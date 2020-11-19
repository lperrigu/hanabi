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
# **************************************************************************** #\

import sys


def player_play(deck, hands, board_state, tokens, current_player = 0):
    while (True):
        ret = False
        print_hands_and_state(hands, board_state)
        print("Que faire joueur " + str(current_player) + " ?")
        inp = input()
        if inp  == 'play':#, 'discard', 'hint']:
            print("Tu joue quelle carte ?")
            inp = input()
            inp = int(inp)
            ret = played(inp, deck, hands, board_state, tokens, current_player)
        elif inp == 'discard':
            print("Tu defausse quelle carte ?")
            inp = input()
            inp = int(inp)
            ret = discarded(inp, deck, hands, board_state,
                            tokens, current_player)
        elif inp == 'hint':
            if tokens['hint'] > 0:
                print("Quelle indice ?")
                inp = input()
                inp = inp.split()
                #inp = [int(i) for i in inp]
                ret = hinted(inp, deck, hands, board_state,
                             tokens, current_player)
            else:
                print("Pas d'indices de dispo !")
        else:
            print("Ce n'est pas une action")
        if ret:
            return True
