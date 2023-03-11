# defines class Card, part of L2-2 & H2

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six",
         "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]

#    here we define constants to represent both ranks and suits more expressively
#   (note use of tuple assignment and  \ to continue statement over two lines)

(ACE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE,TEN,JACK,QUEEN,KING) = \
    (1,2,3,4,5,6,7,8,9,10,11,12,13)
(CLUBS,DIAMONDS,HEARTS,SPADES) = (0,1,2,3)

class Card():
    """
    Card represents a single standard playing card,
    with two int attributes:
      _rank from 1 (Ace) to 13 (King),
      _suit from 0 (Clubs) to 3 (Spades)
    """

    def __init__(self, rank=ACE, suit=SPADES):
        '''
        Initialize card with given int suit 0..3 and int rank 1..13
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self):
        '''
        Return the string name of this card:
        "Ace of Spades":
        Note the use of lists RANKS and SUITS with indexing into these
        translating the int fields to descriptive strings
        '''

        # "Ace of Spades" is string for self._rank==1, self._suit==3

        toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

        return toreturn

    def __gt__(self, other):
        if self._suit > other._suit:
            return True
        elif self._suit < other._suit:
            return False
        else:
            if self._rank == ACE:
                return True
            elif other._rank == ACE:
                return False
            elif self._rank > other._rank:
                return True
            else:
                return False

    def __lt__(self, other):
        if self._suit < other._suit:
            return True
        elif self._suit > other._suit:
            return False
        else:
            if self._rank == ACE:
                return False
            elif other._rank == ACE:
                return True
            elif self._rank < other._rank:
                return True
            else:
                return False

    def __le__(self, other):
        if self._suit <= other._suit:
            return True
        elif self._suit > other._suit:
            return False
        else:
            if self._rank == ACE:
                return False
            elif other._rank == ACE:
                return True
            elif self._rank <= other._rank:
                return True
            else:
                return False

    def __ne__(self, other):
        if self._suit != other._suit:
            return True
        elif self._suit == other._suit:
            if self._rank != other._rank:
                return True
            else:
                return False
        return False

    def __eq__(self, other):
        if self._suit == other._suit:
            return True
        elif self._suit == other._suit:
            if self._rank == other._rank:
                return True
            else:
                return False
        return False

    def __ge__(self, other):
        if self > other or self == other:
            return True
        else:
            return False

def main():
    """
    Create several Cards and print
    Also demonstrate adding new field dynamically...
    """

    card1 = Card(QUEEN, HEARTS)  # Ace of Spades

    # 3 ways of 'stringifying' a Card

    print(card1) # trying to print an object ref calls str(ref) automagically
    print(str(card1))  # function call equivalent to above
    print(card1.__str__())  # long-winded form using 'dunder str'

    # If you have a Card reference, you can access _rank and _suit fields outside class:

    print (card1._rank)
    print (card1._suit)

if __name__ == "__main__": # only run main() if this file isn't imported into another
    main()
