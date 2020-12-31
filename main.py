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
from computer_play import computer_play
from player_play import player_play
from display import print_hands_and_state
from tools import init_deck
import sys

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
            hands[i].append([card[0], card[1], False, False])
            #hands[i].append(deck.pop())
    print("###############################3")
    print(deck)
    print("###############################3")
    print(hands)
    print("###############################3")
    print(board_state)
    print("###############################3")
    tokens = {'error': 0, 'hint': 8}
    current_player = 0
    last_turn = -1
    print_hands_and_state(hands, board_state)
    while True:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print(board_state)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
        if tokens['error'] > 2:
            print("Trop d'erreurs ! C'est perdu !")
            exit(1)
        if last_turn == current_player:
            print("C'est fini !")
            print(board_state)
            exit(1)
        #if current_player == 0:
        #    player_play(deck, hands, board_state, tokens, current_player)
        #else:
        #    print("lol acvanr")
        computer_play(deck, hands, board_state, tokens, current_player)
        print("lol fini")
        print(board_state)
        exit(2)
        current_player = (current_player + 1) % 4
