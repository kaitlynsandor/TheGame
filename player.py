from play import *
from preference import *

class Player:

    def __init__(self):
        self.cards_in_hand = []

    def make_play(self, piles, preferences):
        plays, plays_by_card, self_preferences = self.get_all_possible_moves(piles)


    def get_all_possible_moves(self, piles):
        self.cards_in_hand.sort()
        plays = []
        preferences = []
        plays_by_card = dict()
        for card in self.cards_in_hand:
            card_plays = []
            for pile in piles:
                if pile.start_val == 100:
                    if card < pile.current_value:
                        diff = abs(card - pile.current_value)
                        card_plays.append(Play(card, pile, diff))
                        plays.append(Play(card, pile, diff))
                        if diff < 11:
                            preferences.append(Preference(pile, diff))
                    elif card == pile.current_value + 10:
                        plays.append(Play(card, pile, -1))
                        card_plays.append(Play(card, pile, 0))
                        preferences.append(Preference(pile, 0))
                elif pile.start_val == 1:
                    if card > pile.current_value:
                        diff = abs(card - pile.current_value)
                        plays.append(Play(card, pile, diff))
                        card_plays.append(Play(card, pile, diff))
                        if diff < 11:
                            preferences.append(Preference(pile, diff))
                    elif card == pile.current_value - 10:
                        plays.append(Play(card, pile, -1))
                        card_plays.append(Play(card, pile, 0))
                        preferences.append(Preference(pile, 0))
            plays_by_card[card] = card_plays
        return plays, plays_by_card, preferences

    def pick(self, value, deck):
        for i in range(0, value):
            self.cards_in_hand.append(deck.get_item())