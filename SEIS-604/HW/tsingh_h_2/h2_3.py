# h2_3.py
# Tarun Singh
# starting code for H2 Exercise 3

import deck

# deck.Deck is to be modified by adding __getitem__ method

def main():
    d = deck.Deck()
    d.shuffle()

    # First card
    print(d[0])

    # Second card
    print(d[1])

    # Last card
    print(d[-1])

    # Printing each card in deck
    for i, card in enumerate(d):
        print("Card at index {} is: {}".format(i, d[i]))

main()

