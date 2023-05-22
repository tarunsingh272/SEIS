# lab_2_3.py
# L2-3 Exercise

# add new method to Card named ranksHigher(Card c)
# then add main() code that creates two Cards,
#   and compares them using ranksHigher(Card)

import card
import deck

def main():
    d = deck.Deck()
    d.shuffle()

    card_player = d.deal_card()
    card_dealer = d.deal_card()

    print("Player gets", card_player, "and dealer gets", card_dealer)

    if card_player.ranksHigher(card_dealer):
        print("Player wins")
    else:
        print("Dealer wins")
main()