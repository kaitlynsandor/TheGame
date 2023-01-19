from preference import *
from strategy import *

class LeastSelfHarmStrat(Strategy):

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

        return optimal_moves

    def update_optimal_plays(self, card, plays):
        for play in plays:
            if play.card == card:
                plays.remove(play)
        return plays

    def make_play(self, num_to_play, cards_in_hand, plays, plays_by_card, preferences_to_plays_dict, self_preferences, preferences):

        played_cards = []
        optimal_plays = self.get_optimal_moves(num_to_play, self_preferences, plays, preferences_to_plays_dict)
        while(num_to_play != 0 and len(optimal_plays) != 0):
            play = optimal_plays.pop()
            play.pile.play_card(play.card)
            played_cards.append(play.card)
            num_to_play -= 1
        if(len(optimal_plays) == 0 and num_to_play != 0):
            return played_cards, True
        else:
            return played_cards, False