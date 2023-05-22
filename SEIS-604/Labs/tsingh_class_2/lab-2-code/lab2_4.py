# lab_2_4.py
# L2-4 Exercise

# Implement the __gt__ special method for Card,
#   such that d > c gives the same result as d.ranksHigher(c)
#   of the previous problem

import card
import deck

def main():
    d = deck.Deck()
    d.shuffle()

    card_player = d.deal_card()
    card_dealer = d.deal_card()

    print("Player gets", card_player, "and dealer gets", card_dealer)

    if card_player > card_dealer:
        print("Player wins")
    else:
        print("Dealer wins")

main()
