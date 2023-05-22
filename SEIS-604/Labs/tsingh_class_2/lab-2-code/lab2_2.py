# lab_2_2.py
# L2-2 Exercise:

# Use imported Card, Deck to write a simple game where a new Deck is shuffled,
# then a card is dealt to the player, then another to the dealer.
# Then compare the two cards and announce whose Card has a higher value
# and is thus the winner of the hand.
#

import card
import deck

# card.Card, deck.Deck are imported class names

def main():
    d = deck.Deck()
    d.shuffle()
    print(d)

    card_player = d.deal_card()
    card_dealer = d.deal_card()

    print("Player gets", card_player, "and dealer gets", card_dealer)

    if card_player._suit > card_dealer._suit:
        print("Player wins with ", card_player, " vs ", card_dealer)
    elif card_player._suit < card_dealer._suit:
        print("Dealer wins with ", card_dealer, " vs ", card_player)
    else:
        if card_player._rank == card.ACE:
            print("Player wins with ", card_player, " vs ", card_dealer)
        elif card_dealer._rank == card.ACE:
            print("Dealer wins with ", card_dealer, " vs ", card_player)
        elif card_player._rank > card_dealer._rank:
            print("Player wins with ", card_player, " vs ", card_dealer)
        else:
            print("Dealer wins with ", card_dealer, " vs ", card_player)



main()



