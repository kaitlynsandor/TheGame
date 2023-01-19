from play import *
from preference import *
from leastselfharmstrat import *

class Player:
    GAME_OVER = False
    def __init__(self, name, strategy):
        self.name = name
        self.cards_in_hand = []
        self.strategy = strategy

    def make_play(self, num_to_play, piles, preferences):
        plays, plays_by_card, self_preferences, preferences_to_plays_dict = self.get_all_possible_moves(piles)
        cards_played, game_over = self.strategy.make_play(num_to_play, self.cards_in_hand, plays, plays_by_card, preferences_to_plays_dict, self_preferences, preferences)
        return cards_played, game_over

    def update_cards_in_hand(self, cards_played):
        for card in cards_played:
            self.cards_in_hand.remove(card)

    def get_all_possible_moves(self, piles, diff_sensitivity=100):
        self.cards_in_hand.sort()
        plays = []
        preferences = []
        plays_by_card = dict()
        preferences_to_plays_dict = dict()
        for card in self.cards_in_hand:
            card_plays = []
            for pile in piles:
                if pile.start_val == 100:
                    if card < pile.current_value:
                        diff = abs(card - pile.current_value)
                        play = Play(card, pile, diff)
                        card_plays.append(play)
                        plays.append(play)
                        if diff < diff_sensitivity:
                            preference = Preference(pile, diff)
                            preferences.append(preference)
                            preferences_to_plays_dict[preference] = play
                    elif card == pile.current_value + 10:
                        play = Play(card, pile, 0)
                        preference = Preference(pile, 0)
                        plays.append(play)
                        card_plays.append(play)
                        preferences.append(preference)
                        preferences_to_plays_dict[preference] = play
                elif pile.start_val == 1:
                    if card > pile.current_value:
                        diff = abs(card - pile.current_value)
                        play = Play(card, pile, diff)
                        plays.append(play)
                        card_plays.append(play)
                        if diff < diff_sensitivity:
                            preference = Preference(pile, diff)
                            preferences.append(preference)
                            preferences_to_plays_dict[preference] = play
                    elif card == pile.current_value - 10:
                        play = Play(card, pile, 0)
                        preference = Preference(pile, 0)
                        plays.append(play)
                        card_plays.append(play)
                        preferences.append(preference)
                        preferences_to_plays_dict[preference] = play
            plays_by_card[card] = card_plays
        return plays, plays_by_card, preferences, preferences_to_plays_dict

    def pick(self, value, deck):
        for i in range(0, value):
            self.cards_in_hand.append(deck.get_item())

    def is_game_over(self, piles):
        if Player.GAME_OVER == True:
            return True

        for pile in piles:
            for card in self.cards_in_hand:
                if pile.start_val == 1 and card > pile.current_value:
                    return False
                elif pile.start_val == 100 and card < pile.current_value:
                    return False
        return True