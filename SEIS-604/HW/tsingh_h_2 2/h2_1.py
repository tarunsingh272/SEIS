#
# h2_1.py:
# Tarun Singh
# starting code for H2 Exercise 1

from card import Card
import deck

# card.Card is class to modify

def main():
    d = deck.Deck()
    d.shuffle()

    card_player = d.deal_card()
    card_dealer = d.deal_card()

    print("Player gets", card_player, "and dealer gets", card_dealer)

    # Check __gt__ functionality
    if card_player > card_dealer:
        print("Player wins")
    else:
        print("Dealer wins")

    # Check __lt__ functionality
    if card_player < card_dealer:
        print("Dealer wins")
    else:
        print("Player wins")

    # Check __ne__ functionality
    if card_player != card_dealer:
        print("Different cards")
    else:
        print("Same cards")

    # Check __eq__ functionality
    if card_player == card_dealer:
        print("Same cards")
    else:
        print("Different cards")

    # Check __ge__ functionality
    if card_player >= card_dealer:
        print("Player wins or results in draw")
    else:
        print("Dealer wins")

    # Check __le__ functionality
    if card_player <= card_dealer:
        print("Dealer wins or results in draw")
    else:
        print("Player wins")

main()