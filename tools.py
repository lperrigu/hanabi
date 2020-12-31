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
#from computer_play import computer_play
#from player_play import player_play
#from display import print_hands_and_state
import sys

def init_deck():
    deck = [(1, 'r'), (1, 'r'), (1, 'r'), (2, 'r'), (2, 'r'), (3, 'r'),
            (3, 'r'), (4, 'r'), (4, 'r'), (5, 'r'),
            (1, 'b'), (1, 'b'), (1, 'b'), (2, 'b'), (2, 'b'), (3, 'b'),
            (3, 'b'), (4, 'b'), (4, 'b'), (5, 'b'),
            (1, 'g'), (1, 'g'), (1, 'g'), (2, 'g'), (2, 'g'), (3, 'g'),
            (3, 'g'), (4, 'g'), (4, 'g'), (5, 'g'),
            (1, 'y'), (1, 'y'), (1, 'y'), (2, 'y'), (2, 'y'), (3, 'y'),
            (3, 'y'), (4, 'y'), (4, 'y'), (5, 'y'),
            (1, 'w'), (1, 'w'), (1, 'w'), (2, 'w'), (2, 'w'), (3, 'w'),
            (3, 'w'), (4, 'w'), (4, 'w'), (5, 'w')]
    shuffle(deck)
    return deck


def played(inp, deck, hands, board_state, tokens, current_player):
    color_card_played = hands[current_player][inp][1]
    value_card_played = hands[current_player][inp][0]
    if board_state[color_card_played] == value_card_played - 1:
        board_state[color_card_played] += 1
    else:
        print("Ca ne marche pas ! Erreur !")
        tokens['error'] += 1
    hands[current_player].pop(inp)
    card = deck.pop()
    hands[current_player].append([card[0], card[1], False, False])
    return True


def discarded(inp, deck, hands, board_state, tokens, current_player):
    color_card_played = hands[current_player][inp][1]
    value_card_played = hands[current_player][inp][0]
    if tokens['hints'] < 8:
        tokens['hints'] += 1
    hands[current_player].pop(inp)
    card = deck.pop()
    hands[current_player].append([card[0], card[1], False, False])
    return True


def hinted(inp, deck, hands, board_state, tokens, current_player):
    tokens['hint'] -= 1
    number_hint = False
    color_hint = False
    if inp[1].isdigit():
        number_hint = True
        print("OUI un chiofre")
    elif inp[1].isalpha():
        color_hint = True
        print("OUI un color")
    inp[0] = int(inp[0])
    for i in range(len(hands[inp[0]])):
        if number_hint and hands[inp[0]][i][0] == int(inp[1]):
            hands[inp[0]][i][2] = inp[1]
        if color_hint and hands[inp[0]][i][1] == inp[1]:
            hands[inp[0]][i][3] = inp[1]
    return True
