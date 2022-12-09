import random 

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

#the status of your hand
high_card = False
pocket_pair = False
one_pair = False
two_pair = False
trips = False
straight = False
flush = False
fullhouse = False
quads = False
straight_flush = False
royal_flush = False

#todo: make a function that actually makes the best 5 card hand

def high_card(hand):
    uwu=0

def pair(hand):
    pairs = []

    #checks for all possible pairs in a hand.
    #If there's trips it'll add the same pair three times. quads will be 6 times
    for i in range(len(hand)):
        for f in range(i+1, len(hand)):
            if(hand[i][0] == hand[f][0]):
                pairs.append(hand[i][0])

    return pairs

    #todo: distinct between pair, trips, quads

def two_pair(hand):
    pairs = pair(hand)
    if()

def trips(hand):
    uwu=0

def straight(hand):
    uwu=0

def flush(hand):
    uwu=0

def full_house(hand):
    uwu=0

def quads(hand):
    uwu=0

def straight_flush(hand):
    uwu=0

def royal_flush(hand):
    uwu=0

def pre_flop():