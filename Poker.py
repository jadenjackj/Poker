import random
import Hand
from itertools import combinations

stack = int(input("How much are you buying in for?: "))

pot = 0

computer_stack = stack

cards = ['As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s',
        'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d',
        'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c',
        'Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h'] 

ready = random.shuffle(cards)

player1 = []
computer_play = []

#deals out cards
for i in range(0,4):
    if(i%2 == 0):
        player1.append(cards[i])
    else:
        computer_play.append(cards[i])

flop = cards[5:8]
turn = cards[9]
river = cards[11]
board = []


#so this gets all the possible hand combinations you can get based on what's on the board.
def hand_combinations(player_hand, board, number):
    cards_available = player_hand+board
    possible_hands= list(combinations(cards_available, number))
    return possible_hands

def pre_flop(player_hand, board):
    all_hand_combinations= hand_combinations(player_hand, board, 2) #gets all the possible hand combinations

    #creates a list of hand objects from the hand class with each object holding its own information such as what is in the hand and that particular hand's strength
    hands_object_list= []
    for i in all_hand_combinations:
        hands_object_list.append(Hand(i))

    hands_object_list.sort(key=lambda hand: hand.strength) #sorts the hand object based on hand strength
    

def tie_breaker():
    #question: how do I choose the hand combination that's the strongest? Like suppose one hand is like 23456 and the other is like 34567.
    #todo: figure that shit out^
    #answer: Okay what If we have each strength evaluator function return a list of the winning cards? i.e. quads returns the list of quad numbers, 2 pair returns the 2 pairs, etc.
    uwu=0