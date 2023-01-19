class Play:
    def __init__(self, card, pile, damage):
        self.card = card
        self.pile = pile
        self.damage = damage

    def __repr__(self):
        return "PLAY pile: " + str(self.pile.name) + ' card: ' + str(self.card) + ' damage ' + str(self.damage)