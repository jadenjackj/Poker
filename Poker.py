'''
Create a program where the user can play the computer in a game of Texas hold em 

TO DO:
- Create a way for the program to know what hands are winning over others
---Order of hands:
1) Royal Flush - player has 5 cards of the same suit and they are all face cards
2) Straight Flush - player has all cards of the same suit and they are in sequential order 
3) Four of a Kind(quads) - player has 4 of the same card
4) Full House(boat) - player has made a board where they have 3 of the same card and two of a different card
5) Flush - player has gotten 5 cards of the same suit
6) Straight - player has gotten 5 cards all in sequential order
7) Three of a Kind(trips) - player has three of the same card
8) Two Pair - player has two of the same card and two of a different card
9) One Pair - player has one of the same card 
10)High Card - player has the highest card on the table
---
- Create a way for the program to know what cards are in a deck of 52 note: Done
- Create a way for the program to shuffle the deck note: Done
- Make the program be able to give itself two random cards from the deck and give you two random cards from the deck
- Make sure the program removes the cards from the deck whenever they are given to you, and also when they are dealt out on the board note: done
- Have to have betting amounts and a starting stack (With betting amounts make a variable that subtracts from their stack when the user 
or computer bets and adds to their stack when they win) note: done
- Have the computer know the "flop", "turn, and "river" note: done
- Have to have big and small blinds 
- Have to know words like raise, call, fold, all in note: done
- Have to know when to raise, call, fold, or all in note: done
- Option to have the computer or user be able to buy in more if they lose all of their chips

'''
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
count = 0
z = 0
j = 1

while(count < 3):
    player1.append(cards[z])
    computer_play.append(cards[j])
    z += 2
    j += 2
    count += 2
        
flop = cards[5:8]
turn = cards[9]
river = cards[11]
board = []

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

if player1[0][0] == player1[1][0]:
    pocket_pair = True


g = 0
board_count = 0
while(g < len(board)):
    k = g +1
    board_pair = False
    while(k < len(board)):
        if board[g][0] == board[k][0]:
            board_pair = True
        k += 1
    if board_pair:
        board_count +=1
    g += 1


p = 0
match = 0
match2 = 0

# this while loop is checking for matches in the players hand and in the board
while(p < len(board)):
    if player1[0][0] in board[p]:
        match += 1
    elif player1[1][0] in board[p]:
        match2 += 1
    p += 1


# checking for quads
if pocket_pair and match == 2:
    quads = True
elif match ==3 or match2 == 3:
    quads = True
else:
    quads = quads



# checking for full house
if pocket_pair and match == 1 and board_count == 2:
    fullhouse = True
elif match == 2 and board_count ==2 or match2 == 2 and board_count == 2:
    fullhouse = True
elif board_count == 3:
    fullhouse = True
else:
    fullhouse = False

# note: checking for one pair
if match == 1 or match2 == 1:
    one_pair = True
elif pocket_pair:
    one_pair = True

# note: checking for two pair
if board_count == 2 and match == 1:
    one_pair = False
    two_pair = True
elif board_count == 2 and match2 == 1:
    one_pair = False
    two_pair = True
elif match == 1 and match2 == 1:
    one_pair = False
    two_pair = True

# note: checking for trips 
if match == 2 or match2 == 2:
    trips = True
elif pocket_pair and match == 1:
    one_pair = False
    trips = True

def start():
    global stack
    global computer_stack
    global pot

    w = 0
    while(w<3):
        board.append(flop[w])
        w +=1
    
    play_now = input("Hi my name is Soju the computer do you want to play poker with me?: ")
    if play_now == 'yes':
        print("Your hand is " + ' '.join(player1) + ".")
        print("The flop is " + ' '.join(board))
    else:
        print("Okay thanks anyway!")

    computer = random.choice(['check', 'raise', 'fold'])
    computer2 = random.choice(['fold', 'call', 'all-in'])
    computer3 = random.choice(['fold', 'call', 'all-in'])

    play = input("Check, Raise, or Fold: ")

    if play == "check" and computer == 'check':
        print("Okay let's see the turn")
        middle()
    elif play == "check" and computer == 'raise':
        computer_bet = random.randint(1,stack)
        computer_stack -= computer_bet
        pot += computer_bet
        print("Soju raised by " + str(computer_bet))
        choice = input("Do you want to call, fold, or raise?: ")
        if choice == 'fold':
            return("You lost this hand gang")
        elif choice == 'call':
            call = int(input("Okay, bet the same amount: "))
            stack -= call
            pot += call
            if call == computer_bet:
                middle()
        elif choice == 'raise':
            raise1 = int(input("What do you want to raise to?: "))
            stack -= raise1
            pot += raise1
            if raise1 > computer_bet:
                print("Soju has chosen to " + computer2)
                if computer2 == 'fold':
                    print("You won gang")
                    stack += pot
                    return("Your stack is " + str(stack))
                elif computer2 == 'call':
                    pot += (raise1 - computer_bet)
                    print("I'll call that bet, let's see the turn")
                    middle()
                elif computer2 == 'all-in':
                    pot += computer_bet
                    final_choice = input("I'm all-in, call or fold?: ")
                    if final_choice == 'call':
                        pot += stack
                        end()
                    elif final_choice == 'fold':
                        print("You lost this hand gang and your stack is " + str(stack))
    elif play == 'check' and computer == 'fold':
        return("You won the hand gang, your stack is " + str(stack))
    elif play == 'raise':
        how = int(input("How much do you want to raise by?: "))
        if computer == 'fold':
            play_again = input("Nice raise I guess I'll fold, do you want to play another hand?: ")
            if play_again == 'yes':
                start()
            else:
                print("Okay, nice hand see you later")
        elif computer == 'check':
            if computer3 == 'fold':
                play_again2 = input("nice hand, play again?: ")
                if play_again2 == 'yes':
                    start()
                else:
                    return("okay")
            elif computer3 == 'call':
                print("I'll call that bet, let's see the turn")
                middle()
            elif computer3 == 'all-in':
                final_choice2 = input("I'm all in, call or fold?:")
                if final_choice2 == 'call':
                    pot += stack
                    end()
                elif final_choice2 == 'fold':
                    print("You lost this hand gang and your stack is " + str(stack))
        elif computer == 'raise':
            raise_range = stack - how
            computer_raise = random.randint(raise_range,stack)
            pot += computer_raise
            fly = input("I've raise you by " + str(computer_raise) + " call, fold, or all-in")
            if fly == 'fold':
                print("Nice hand")
            elif fly == 'call':
                call_that = int(input("Okay, match my chips: "))
                call_these = computer_raise + how 
                if call_that == call_these:
                    middle()
            elif fly == 'all in':
                stack += pot 
                end()




    


def middle():
    global stack
    global pot

    w = 0 
    while (w<1):
        board.append(turn)
        w +=1

    print(' '.join(board))

    play2 = input("Check, Raise, or Fold: ")

    if play2 == "check":
        end()
    elif play2 == "raise":
        how2 = int(input("How much?: "))
        pot += how2
        end()
    else:
        print("You lost " + str(how2) + "$ and your stack is " + str(stack) + "$.")

def end():
    global stack 

    w = 0 
    while (w<1):
        board.append(river)
        w +=1

    print(' '.join(board))
    
    play3 = input("Check, Raise, or Fold: ")

    if play3 == "raise":
        how3 = int(input("How much?: "))
        stack -= how3 

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

    if player1[0][0] == player1[1][0]:
        pocket_pair = True


    g = 0
    board_count = 0
    while(g < len(board)):
        k = g +1
        board_pair = False
        while(k < len(board)):
            if board[g][0] == board[k][0]:
                board_pair = True
            k += 1
        if board_pair:
            board_count +=1
        g += 1


    p = 0
    match = 0
    match2 = 0

    # this while loop is checking for matches in the players hand and in the board
    while(p < len(board)):
        if player1[0][0] in board[p]:
            match += 1
        elif player1[1][0] in board[p]:
            match2 += 1
        p += 1
    
    # high card 
    if match == 0 or match2 == 0:
        high_card = True 


    # checking for quads
    if pocket_pair and match == 2:
        quads = True
    elif match ==3 or match2 == 3:
        quads = True
    else:
        quads = quads



    # checking for full house
    if pocket_pair and match == 1 and board_count == 2:
        fullhouse = True
    elif match == 2 and board_count ==2 or match2 == 2 and board_count == 2:
        fullhouse = True
    elif board_count == 3:
        fullhouse = True
    else:
        fullhouse = False

    # note: checking for one pair
    if match == 1 or match2 == 1:
        one_pair = True
    elif pocket_pair:
        one_pair = True

    # note: checking for two pair
    if board_count == 2 and match == 1:
        one_pair = False
        two_pair = True
    elif board_count == 2 and match2 == 1:
        one_pair = False
        two_pair = True
    elif match == 1 and match2 == 1:
        one_pair = False
        two_pair = True

    # note: checking for trips 
    if match == 2 or match2 == 2:
        trips = True
    elif pocket_pair and match == 1:
        one_pair = False
        trips = True
    # checking for straight
    low = False
    low1 = False
    low2 = False
    low3 = False
    low4 = False

    for a in board:
        if a[0] == 'A': 
            low = True
        elif a[0] == '2': 
            low1 = True
        elif a[0] == '3': 
            low2 = True
        elif a[0] == '4': 
            low3 = True
        elif a[0] == '5': 
            low4 = True

    for s in player1:
        if s[0] == 'A': 
            low = True
        elif s[0] == '2': 
            low1 = True
        elif s[0] == '3': 
            low2 = True
        elif s[0] == '4': 
            low3 = True
        elif s[0] == '5': 
            low4 = True

    straight_list = []

    for v in board:
        straight_list.append(v[0])
        if v[0] == 'T':
            straight_list.append('10')
        elif v[0] == 'J':
            straight_list.append('11')
        elif v[0] == 'Q':
            straight_list.append('12')
        elif v[0] == 'K':
            straight_list.append('13')
        elif v[0] == 'A':
            straight_list.append('14')

    for b in player1:
        straight_list.append(b[0])
        if b[0] == 'T':
            straight_list.append('10')
        elif b[0] == 'J':
            straight_list.append('11')
        elif b[0] == 'Q':
            straight_list.append('12')
        elif b[0] == 'K':
            straight_list.append('13')
        elif b[0] == 'A':
            straight_list.append('14')

    if low and low1 and low2 and low3 and low4:
        straight_list.append('1')
        straight_list.remove('14')

    for m in straight_list:
        if 'A' in straight_list:
            straight_list.remove('A')
        elif 'K' in straight_list:
            straight_list.remove('K')
        elif 'Q' in straight_list:
            straight_list.remove('Q')
        elif 'J' in straight_list:
            straight_list.remove('J')
        elif 'T' in straight_list:
            straight_list.remove('T')
        else:
            straight_list = straight_list

    straight_set = [*set(straight_list)]

    straight_order = sorted(straight_set, key=int)

    straight_join = ''.join(straight_order)

    straight_numbers = '1234567891011121314'

    if straight_join[1:6] in straight_numbers or straight_join[0:5] in straight_numbers or straight_join[2:] in straight_numbers:
        straight = True
    # checking for straight flush
    if straight and flush:
        straight_flush = True
    # checking for royal flush 
    if straight_order[0] == '10' and flush:
        royal_flush = True


    if royal_flush:
        stack -= stack
        stack += 500 
        stack += 90
        print("You have a royal flush and your stack is " + str(stack))
    elif straight_flush:
        stack -= stack
        stack += 500 
        stack += 80
        print("You have a straight flush and your stack is " + str(stack))
    elif quads:
        stack -= stack
        stack += 500 
        stack += 70
        print("You have quads and your stack is " + str(stack))
    elif fullhouse:
        stack -= stack
        stack += 500 
        stack += 60
        print("You have a boat and your stack is " + str(stack))
    elif flush:
        stack -= stack
        stack += 500 
        stack += 50
        print("You have a flush and your stack is " + str(stack))
    elif straight and not one_pair and not two_pair and not trips and not flush and not fullhouse:
        stack -= stack
        stack += 500 
        stack += 40
        print("You have a straight and your stack is " + str(stack))
    elif trips:
        stack -= stack
        stack += 500 
        stack += 30
        print("You have trips and your stack is " + str(stack))
    elif two_pair:
        stack -= stack
        stack += 500 
        stack += 20
        print("You have two pair and your stack is " + str(stack))
    elif one_pair:
        stack -= stack
        stack += 500 
        stack += 10
        print("You have one pair and your stack is " + str(stack))
    elif high_card:
        stack = stack
    else:
        stack = stack


start()