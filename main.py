from deck import *
from pile import *
from player import *

if __name__ == "__main__":
    DECK = Deck()
    pile_1_1 = Pile(1)
    pile_1_2 = Pile(1)
    pile_100_1 = Pile(100)
    pile_100_2 = Pile(100)

    piles = [pile_1_1, pile_1_2, pile_100_1, pile_100_2]

    players = [Player(LeastHarmStrat()), Player(LeastHarmStrat()), Player(LeastHarmStrat()), Player(LeastHarmStrat())]

    for player in players:
        player.pick(6, DECK)

    i = 0
    current_player = players[i]

    while(not current_player.is_game_over(piles)):
        all_other_preferences = []
        for player in players:
            if player != current_player:
                plays, plays_by_card, preferences = player.get_all_possible_moves(piles)
                all_other_preferences += preferences

        played_cards = current_player.make_play(piles, all_other_preferences)
        current_player.update_cards_in_hand(played_cards)
        current_player.pick(len(played_cards), DECK)

        if i < 3:
            i += 1
        else:
            i = 0

        current_player = players[i]

    for pile in piles:
        print(pile.pile_cards)

    print(DECK.deck)

