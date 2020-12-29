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

from random import shuffle
import sys

def print_hands_and_state(hands, board_state):
    color_print = {'r':str('\x1b[0;30;41m'),
                   'b':str('\x1b[0;30;44m'),
                   'g':str('\x1b[0;30;42m'),
                   'y':str('\x1b[0;30;43m'),
                   'w':str('\x1b[0;30;47m'),
                   'end':str('\x1b[0m')}
    print("Composition des feux d'artifices :")
    print('\x1b[0;30;41m' + str(board_state['r']) + '\x1b[0m' + '   '
        + '\x1b[0;30;42m' + str(board_state['g']) + '\x1b[0m' + '   '
        + '\x1b[0;30;47m' + str(board_state['w']) + '\x1b[0m' + '   '
        + '\x1b[0;30;44m' + str(board_state['b']) + '\x1b[0m' + '   '
        + '\x1b[0;30;43m' + str(board_state['y']) + '\x1b[0m')
    print("\n\nMains des joueurs")
    for i in range(len(hands)):
        str_print = ''
        print("\nJoueur " + str(i) + " :")
        for j in range(len(hands[i])):
            str_print += ('   ' + color_print[hands[i][j][1]]
                          + str(hands[i][j][0]) + color_print['end'] + '   ')
        str_print += '\n '
        for j in range(len(hands[i])):
            hint_number = '?' if hands[i][j][2] is False else hands[i][j][2]
            hint_color = '?' if hands[i][j][3] is False else hands[i][j][3]
            str_print += hint_number + '   ' + hint_color + '  '
        print(str_print)
#123*123*123*
#1*123*123
