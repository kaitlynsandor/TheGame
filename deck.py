import random

class Deck:
    def __init__(self):
        self.deck = list(range(2,99))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deck_size(self):
        return len(self.deck)

    def empty_deck(self):
        return len(self.deck) == 0

    def get_item(self):
        return self.deck.pop()
