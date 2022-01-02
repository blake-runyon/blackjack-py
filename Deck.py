import random

from Card import *


class Deck:
    cards = []

    def __init__(self, num_decks):
        for decks in range(num_decks):
            for i in range(4):
                for j in range(13):
                    self.cards.append(Card(i, j))

    def print_deck(self):
        for x in self.cards:
            print(x.get_rank() + " of " + x.get_suit() + " Value: " + str(x.get_score()))

    def deal_card(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)