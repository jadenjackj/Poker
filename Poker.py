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


#todo: make a function that actually makes the best 5 card hand
#question: how do we actually determine what are the best 5 cards without running the hand through the program?
#answer: Why not just run every combination of the hands through the program?
#note: with 5 cards in the river and 2 cards in hand, we have 21 possible combinations

#question: how are we gonna keep track of the boolean variables for each hand?
#answer: alright so here's what I'm thinking. We have a hand class and each hand is an instance of that class with the boolean values connected to it
#todo: make the hands class with the features of a hand like the type of hand and the cards in the hand


#so this gets all the possible hand combinations you can get based on what's on the board.
def hand_combinations(player_hand, board, number):
    cards_available = player_hand+board
    possible_hands= list(combinations(cards_available, number))
    return possible_hands

def pre_flop(player_hand, board):
    all_hand_combinations= hand_combinations(player_hand, board, 2) #gets all the possible hand combinations

    #creates a list of hand objects with each object holding its own information such as what is in the hand and that particular hand's strength
    possible_hands_list= []
    for i in all_hand_combinations:
        possible_hands_list.append(Hand(i))