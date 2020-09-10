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


def print_hands_and_state(hands, board_state):
    print("Composition des feux d'artifices :")
    print('\x1b[0;30;41m' + str(board_state['r']) + '\x1b[0m' + '   '
        + '\x1b[0;30;42m' + str(board_state['g']) + '\x1b[0m' + '   '
        + '\x1b[0;30;47m' + str(board_state['w']) + '\x1b[0m' + '   '
        + '\x1b[0;30;44m' + str(board_state['b']) + '\x1b[0m' + '   '
        + '\x1b[0;30;43m' + str(board_state['y']) + '\x1b[0m')
    print("\n\nMains des joueurs")


def play(deck, hands, board_state, token):
    while (True):
        print_hands_and_state(hands, board_state)
        print("Que faire ?")
        inp = input()
        if inp  == 'play':#, 'discard', 'hint']:
            print("Tu joue quelle carte ?")
            inp = input()
            inp = int(inp)
            played(inp)
        elif inp == 'discard':
            print("Tu defausse quelle carte ?")
            inp = input()
            inp = int(inp)
            discarded(inp)
        elif inp == 'hint':
            print("Indice sur quelle joueur ?")
            inp = input()
            inp = int(inp)
            hinted(inp)
        else:
            print("Ce n'est pas une action")


if __name__ == '__main__':
    deck = init_deck()
    board_state={'r':0, 'b':0, 'g':0, 'y':0, 'w':0}
    if len(sys.argv) > 2:
        print("NOPE")
        exit(1)
    elif len(sys.argv) == 1:
        number_player = 2
    elif sys.argv[1].isdigit():
        number_player = int(sys.argv[1])
    else:
        print("NOPE AGAIN")
        exit(1)
    if number_player > 5 or number_player < 2:
        print("Le nombre de joueur doit etre de 2 minimum ou 5 maximum")
        exit(1)
    hands = []
    if number_player < 4:
        hand_size = 5
    else:
        hand_size = 4
    for i in range(number_player):
        hands.append([])
        for j in range(hand_size):
            card = deck.pop()
            hands[i].append([card[0], card[1], -1, -1])
            #hands[i].append(deck.pop())
    print("###############################3")
    print(deck)
    print("###############################3")
    print(hands)
    print("###############################3")
    print(board_state)
    print("###############################3")
    #error = 0
    #hints = 8
    tokens = {'error': 0, 'hint': 8}
    current_player = 0
    last_turn = -1
    print_hands_and_state(hands, board_state)
    print('tjghjghghghgr')
    exit(1)
    while True:
        if tokens['error'] > 2:
            print("Trop d'erreurs ! C'est perdu !")
            exit(1)
        if last_turn == current_player:
            print("C'est fini !")
            print(board_state)
            exit(1)
        #if current_player == 0:
        play(deck, hands, board_state, token, current_player)
        current_player = (current_player + 1) % 4
