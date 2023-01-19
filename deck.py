import random

class Deck:
    def __init__(self):
        self.deck = list(range(2, 100))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deck_size(self):
        return len(self.deck)

    def empty_deck(self):
        return len(self.deck) == 0

    def get_item(self):
        return self.deck.pop()

    def get_num_to_play(self):
        if self.empty_deck():
            return 1
        else:
            return 2
