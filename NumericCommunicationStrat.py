from preference import *
from strategy import *

class NumericComunicationStrat(Strategy):

        def __init__(self):
            super().__init__()

        def get_pref_by_pile(self, preferences):
            pref_by_pile = [Preference(0, 100), Preference(1, 100), Preference(2, 100), Preference(3, 100)]
            for preference in preferences:
                if preference.desire < pref_by_pile[preference.pile].desire:
                    pref_by_pile[preference.pile] = preference
            return pref_by_pile

        def get_optimal_moves(self, self_pref_by_pile, other_pref_by_pile, plays):
            viable_moves = []
            for i in range(0, 4):
                if self_pref_by_pile[i].desire <= other_pref_by_pile[i].desire:
                    for play in plays:
                        diff = abs(play.card - play.pile.current_value)
                        if play.pile.name == i:
                            if diff == self_pref_by_pile[i].desire:
                                viable_moves.append(play)
                            elif play.card - play.pile.current_value == 10 and play.pile.start_val == 100:
                                viable_moves.append(play)
                            elif play.pile.current_value - play.card == 10 and play.pile.start_val == 1:
                                viable_moves.append(play)
            return viable_moves

        def make_play(self, num_to_play, cards_in_hand, plays, plays_by_card, preferences_to_plays_dict, self_preferences, preferences):
            # get top preference for each by pile
            # if your preference is better for the pile add it to a viable play list
            # play two best from viable play list
            #
            # play all in viable play list
            # if a play is still needed
            # pick pile with least desired preferences from other players
            # when should I keep playing cards?
            # when you have a sequence of cards directly (or indirectly when accounting for current low/high)
            # when you have a 10 off from a card currently in your hand that helps a pile

            self_pref_by_pile = self.get_pref_by_pile(self_preferences)
            other_pref_by_pile = self.get_pref_by_pile(preferences)

            optimal_moves = self.get_optimal_moves(self_pref_by_pile, other_pref_by_pile)

            played_cards = []
            if len(optimal_moves) > 1:
                for play in optimal_moves:
                    play.pile.play_card(play.card)
                    played_cards.append(play.card)
            return played_cards