class Preference:
    def __init__(self, pile, desire):
        self.pile = pile
        self.desire = desire

    def __repr__(self):
        return 'PREFERENCE pile: ' + str(self.pile.name) + ' desire: ' + str(self.desire)