from random import shuffle


def show_hand(name, hand):
    # Lists of strings to represent cards
    suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
    ranks = ["2", "3", "4", "5", "6", "7", "8",
             "9", "10", "Jack", "Queen", "King", "Ace"]

    print("\n", name, "'s Hand", sep="")
    for card in hand:
        print(ranks[card % 13], "of", suits[card // 13])


def main():
    # Initialize the deck
    cards = list(range(52))

    # Shuffle the deck
    shuffle(cards)

    # Create an empty list for each player
    north = []
    east = []
    south = []
    west = []

    # Deal the deck to four players
    while len(cards) != 0:
        east.append(cards.pop(0))
        south.append(cards.pop(0))
        west.append(cards.pop(0))
        north.append(cards.pop(0))

    # Sort the hands
    north.sort()
    east.sort()
    south.sort()
    west.sort()

    # Show the hands
    show_hand("North", north)
    show_hand("East", east)
    show_hand("South", south)
    show_hand("West", west)


main()
