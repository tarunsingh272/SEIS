# part of L2-2...

import random
import card

class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """

    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(card.ACE, card.KING+1):
            for suit in range(card.CLUBS,card.SPADES+1):
                c = card.Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of all Card names,
        in deck order separated by '\n' for easier reading
        '''

        deck_str_to_return = ''

        # You can visit every card in deck this way:
        #
        # for index in range(len(self._cards)):
        #     "access self._cards[index]"
        #
        # but it's easier to do it like this:

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            deck_str_to_return = deck_str_to_return + temp + "\n"  # note \n at end

        return deck_str_to_return

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def deal_card(self):
        try:
            top_card = self._cards.pop(0)  # get and remove top card from deck
        except Exception:
            print ("You emptied the Deck!  Refilling...")
            self.__init__() # refill the deck...
            self.shuffle()
            top_card = self._cards.pop(0)  # get and remove top card from deck

        return top_card

    def deal_hand(self):
        new_hand = hand.Hand() # creates a new empty Hand
        for count in range(5):
            card = self.deal_card()
            new_hand.add_card(card)
        return new_hand

def main():
    '''
    Create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''

    deck = Deck()
    print(str(deck))

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))

    card_1 = deck.deal_card()
    card_2 = deck.deal_card()

    print("The first card dealt is", card_1, "and the second is", card_2)
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


# only run main() if we're not importing it...
if __name__ == "__main__":
    main()
