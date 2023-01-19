class Pile:
    played_cards = []
    completed_low = 1
    completed_high = 100

    def __init__(self, name, start_val):
        self.name = name
        self.current_value = start_val
        self.start_val = start_val
        self.pile_cards = [start_val]

    def play_card(self, card):
        self.pile_cards.append(card)
        Pile.played_cards.append(card)
        if self.start_val == 100 and card - self.current_value == 10:
            self.current_value = card
        elif self.start_val == 1 and self.current_value - card == 10:
            self.current_value = card
        else:
            self.current_value = card

    def __repr__(self):
        return str(self.name) +  ' ' + str(self.pile_cards)