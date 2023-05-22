#  L2-5:  hand.py
#  Finish this as described in L2-5

import card as c
import deck as d

class Hand():
    """
    Hand represents an ordered list of 0 or more Cards,
    with one list attribute: _cards_in_hand

    Each card in the hand has its Card ref as an element of _cards_in_hand.

    """

    def __init__(self):
        '''
        initialize this hand (referenced by self)
            so _cards_in_hand is the empty list
        '''
        self._cards_in_hand = []

    def __str__(self):
        '''
        return a string with each Card c in _cards_in_hand
            added to result, followed by '\t' (tab)
        '''
        to_return = 'hand: ('

        # finish this

        for each_card in self._cards_in_hand:
            to_return += str(each_card) + '\t'

        return to_return + ')'

    def add_card(self,card_to_add):
        '''
        add card_to_add to _cards_in_hand by appending
            to it
        '''
        self._cards_in_hand.append(card_to_add)


def main():
    """
    Create a Deck, shuffle, then create two Hands by
        dealing 10 cards, alternating.
    """
    deck = d.Deck() # creates new Deck
    hand1 = Hand() # creates a new empty Hand
    hand2 = Hand() # ditto

    # deck.shuffle()

    for count in range(5):
        hand1.add_card( deck.deal_card() )
        hand2.add_card( deck.deal_card() )

    print (str(hand1))
    print (str(hand2))

if __name__ == "__main__":
    print(__name__)
    main()
