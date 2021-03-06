# File  name: deck.py
# Author: Yolanda Theodorakis
# Description: Deck class

import random
import card

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(1, 14):
                self.cards.append(card.Card(s, v))

    def show_deck(self):
        for c in self.cards:
            c.show_card()

    def shuffle_deck(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop()
