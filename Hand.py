import numbers

class Hand:
    def __init__(self, hand) -> int:

        #the status of your hand
        self.high_card = False
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


    #todo:
    #converts the hand into a hand I can evaluate numbers wise. converts the jack to 11, queen to 12, etc.
    def convert(hand):
        converted_hand = []
        for i in hand:
            if(i == 'J'):
                converted_hand.append(11)

#----------------------------------------------------------------------------------------------------

    #note: all the functions below determines if a hand has a particular strength
    def quads(self):
        duplicates = duplicates(self.hand)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for i in ranks:
            if(duplicates.count(i) == 6):
                self.quads=True


    def trips(self):
        duplicates = duplicates(self.hand)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for i in ranks:
            if(duplicates.count(i) == 3):
                self.trips=True
    
    #evaluates both one_pair and two_pair
    def pairs(self):
        duplicates = duplicates(self.hand)
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for i in ranks:
            if(duplicates.count(i) == 2 and self.one_pair == True):
                self.two_pair=True
                self.one_pair=False #doing this because if we have a two pair then that means we don't simply have just a one pair anymore
            if(duplicates.count(i) == 2):
                self.one_pair=True

