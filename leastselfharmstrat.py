from preference import *
from strategy import *
from play import *

class LeastSelfHarmStrat(Strategy):
    # plays while cards are 1 away from eachother or 10 away
    # (does not account for 10 away that becomes apparent after playing mroe cards)
    # tries to minimize own personal risk
    def __init__(self):
        super().__init__()

    def sort_preferences(self, preferences):
        preferences.sort(key=lambda x: x.desire)
        return preferences


    def get_optimal_moves(self, num_to_play, self_preferences, plays, preferences_to_plays_dict):
        seen_cards = []
        optimal_moves = []

        if len(self_preferences) == 0:
            for play in plays:
                if play.card not in seen_cards:
                    optimal_moves.append(play)
                    seen_cards.append(play.card)
            return optimal_moves

        self_preferences = self.sort_preferences(self_preferences)

        for preference in self_preferences:
            move = preferences_to_plays_dict[preference]
            if move.card not in seen_cards:
                optimal_moves.append(move)
                seen_cards.append(move.card)
        if len(optimal_moves) < num_to_play:
            plays.sort(key=lambda x: x.damage)
            for play in plays:
                if play.card not in seen_cards:
                    optimal_moves.append(play)
                    seen_cards.append(play.card)
        # print("MOVES LIST")
        # for move in optimal_moves:
        #     print(move)
        # print()
        return optimal_moves

    def update_optimal_plays(self, card, plays):
        for play in plays:
            if play.card == card:
                plays.remove(play)
        return plays

    def is_valid_play(self, play):
        if play.pile.start_val == 1:
            if play.card > play.pile.current_value:
                return True
            return False
        else:
            if play.card < play.pile.current_value:
                return True
            return False


    def make_play(self, piles, num_to_play, cards_in_hand, preferences):
        plays, plays_by_card, self_preferences, preferences_to_plays_dict = self.get_all_possible_moves(piles, cards_in_hand)

        played_cards = []
        optimal_plays = self.get_optimal_moves(num_to_play, self_preferences, plays, preferences_to_plays_dict)
        while(num_to_play != 0 and len(optimal_plays) != 0):
            play = optimal_plays.pop(0)
            if self.is_valid_play(play) and play.card not in played_cards:
                play.pile.play_card(play.card)
                played_cards.append(play.card)
                num_to_play -= 1

        if len(optimal_plays) == 0:
            if num_to_play != 0:
                return played_cards, True
            else:
                return played_cards, False

        else:
            plays, plays_by_card, self_preferences, preferences_to_plays_dict = self.get_all_possible_moves(piles, cards_in_hand, diff_preference_sensitivity=100)
            optimal_plays = self.get_optimal_moves(num_to_play, self_preferences, plays, preferences_to_plays_dict)

            while len(optimal_plays) > 0:
                play = optimal_plays.pop(0)
                if abs(play.card - play.pile.current_value) < 2 or play.damage == 0:
                    if self.is_valid_play(play) and play.card not in played_cards:
                        play.pile.play_card(play.card)
                        played_cards.append(play.card)
            return played_cards, False
    def get_all_possible_moves(self, piles, cards_in_hand, diff_preference_sensitivity=100):
        cards_in_hand.sort()
        plays = []
        preferences = []
        plays_by_card = dict()
        preferences_to_plays_dict = dict()
        for card in cards_in_hand:
            card_plays = []
            for pile in piles:
                if pile.start_val == 100:
                    if card < pile.current_value:
                        diff = abs(card - pile.current_value)
                        play = Play(card, pile, diff)
                        card_plays.append(play)
                        plays.append(play)
                        if diff < diff_preference_sensitivity:
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
                        if diff < diff_preference_sensitivity:
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