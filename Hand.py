import numbers

class Hand:
    def __init__(self, hand) -> int:

        #the status of your hand
        self.high_card = 0 #note: I'm changing high_card to an int because we need to know what's the high card anyways
        self.pocket_pair = False
        self.one_pair = False
        self.two_pair = False
        self.trips = False
        self.straight = False
        self.flush = False
        self.fullhouse = False
        self.quads = False
        self.straight_flush = False
        self.royal_flush = False

        self.strength = 0; #on a scale of 0-10 where 0 is a high card and 10 is a royal flush

        self.hand = hand

        self.tie_breaker = []

#-----------------------------------------------------------------------------------------------------

    #HELPER FUNCTIONS:
    #Gets all the matching cards
    def duplicates(hand):
        #checks for all possible pairs in a hand.
        #If there's trips it'll add the same pair three times. quads will be 6 times
        duplicates = []
        for i in range(len(hand)):
            for f in range(i+1, len(hand)):
                if(hand[i][0] == hand[f][0]):
                    duplicates.append(hand[i][0])
        return duplicates


    #converts the hand into a hand I can evaluate numbers wise. converts the jack to 11, queen to 12, etc.
    def convert_hand(hand, low_or_high):
        converted_hand = []
        for i in hand:
            if(i == 'T'):
                converted_hand.append(10)
            elif(i == 'J'):
                converted_hand.append(11)
            elif(i == 'Q'):
                converted_hand.append(12)
            elif(i == 'K'):
                converted_hand.append(13)
            elif(i == 'A' and low_or_high == 'high'):
                converted_hand.append(14)
            elif(i == 'A' and low_or_high == 'low'):
                converted_hand.append(1)
            else:
                converted_hand.append(int(i))
        return converted_hand

#----------------------------------------------------------------------------------------------------

    #note: all the functions below determines if a hand has a particular strength
    def quads(self):
        duplicate_list = self.duplicates(self.hand)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for i in ranks:
            if(duplicate_list.count(i) == 6):
                self.quads=True
                self.tie_breaker = [i, i, i, i]


    def trips(self):
        duplicate_list = self.duplicates(self,self.hand)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for i in ranks:
            if(duplicate_list.count(i) == 3):
                self.trips=True
                self.tie_breaker = [i, i, i]
    
    #evaluates both one_pair and two_pair
    def pairs(self):
        duplicate_list = self.duplicates(self.hand)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        for i in ranks:
            if(duplicate_list.count(i) == 2 and self.one_pair == True):
                self.two_pair=True
                self.one_pair=False #doing this because if we have a two pair then that means we don't simply have just a one pair anymore
                self.tie_breaker.append(i)
                self.tie_breaker.append(i)
            if(duplicate_list.count(i) == 2):
                self.tie_breker = []
                self.one_pair=True
                self.tie_breaker.append(i)
                self.tie_breaker.append(i)


    def straight(self):
        #2 possible converted hands because Ace an be either 1 strength or 14 strength
        low_converted_hand = self.convert_hand(self.hand, 'low')
        high_converted_hand = self.convert_hand(self.hand, 'high')
        low_converted_hand.sort() #sorts the converted hand from smallest to largest
        high_converted_hand.sort()

        low_straight = True
        high_straight = True
        #if one of the cards is not one less than the next than it ain't a straight
        #checks to see if we have a straight with either A = 1 or A = 14
        for i in range(1,len(low_converted_hand)):
            if(low_converted_hand[i-1]+1 != low_converted_hand[i]):
                low_straight = False
        for i in range(1,len(high_converted_hand)):
            if(high_converted_hand[i-1]+1 != high_converted_hand[i]):
                high_straight = False

        if(low_straight or high_straight):
            self.straight = True
            self.tie_breaker = self.hand #todo: is this right? figure it out because we need to order it


    def flush(self):
        suit = self.hand[0][1] #gets the suit that the flush is supposed to follow
        self.flush = True
        for i in self.hand: #if one of the cards doesn't have the suit then it ain't a flush
            if(i[1] != suit):
                self.flush = False
            #todo: get highest card


    def high_card(self):
        converted_hand = self.convert_hand(self.hand, 'high')
        converted_hand.sort()
        #todo: change it back to the string later bc if we add it now it'll be something like 14 instead of Ace
        self.tie_breaker = [converted_hand[-1]] #returns the highest card value


    #todo: do all the stuff below later

    def straight_flush(self):
        if(self.flush and self.straight):
            self.straight_flush = True


    def full_house(self):
        if(self.trips and self.one_pair):
            self.fullhouse = True


    def royal_flush(self):
        if(self.straight_flush):
            converted_hand = self.convert_hand(self.hand, 'high')
            if(converted_hand[0] == 10 and converted_hand[-1] == 14):
                self.royal_flush = True


    def evaluate(self):
        if(self.royal_flush):
            self.strength = 10
        elif(self.straight_flush):
            self.strength = 9
        elif(self.quads):
            self.strength = 8
        elif(self.fullhouse):
            self.strength = 7
        elif(self.flush):
            self.strength = 6
        elif(self.straight):
            self.strength = 5
        elif(self.trips):
            self.strength = 4
        elif(self.two_pair):
            self.strength = 3
        elif(self.pairs):
            self.strength = 2
        else:
            self.strength = 1 #high card