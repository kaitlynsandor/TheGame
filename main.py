from deck import *
from pile import *
from player import *
from GameState import *

if __name__ == "__main__":
    DECK = Deck()
    # DECK.shuffle_deck()

    pile_1_1 = Pile(0, 1)
    pile_1_2 = Pile(1, 1)
    pile_100_1 = Pile(2, 100)
    pile_100_2 = Pile(3, 100)

    piles = [pile_1_1, pile_1_2, pile_100_1, pile_100_2]

    players = [Player(0, LeastSelfHarmStrat()), Player(1, LeastSelfHarmStrat()), Player(2, LeastSelfHarmStrat()), Player(3, LeastSelfHarmStrat())]

    for player in players:
        player.pick(6, DECK)

    i = 0
    current_player = players[i]


    while(not current_player.is_game_over(piles)):
        player_hands = []
        for player in players:
            player_hands.append(player.cards_in_hand)

        print(GameState(DECK.empty_deck(), piles, player_hands, current_player.name, DECK))

        num_to_play = DECK.get_num_to_play()

        all_other_preferences = []
        for player in players:
            if player != current_player:
                plays, plays_by_card, preferences, preference_to_play_dict = player.get_all_possible_moves(piles)
                all_other_preferences += preferences

        played_cards, game_over = current_player.make_play(num_to_play, piles, all_other_preferences)
        Player.GAME_OVER = game_over

        current_player.update_cards_in_hand(played_cards)

        if not game_over:
            current_player.pick(len(played_cards), DECK)

            if i < 3:
                i += 1
            else:
                i = 0

            current_player = players[i]

    total_cards_left_in_hands = 0
    for hand in player_hands:
        total_cards_left_in_hands += len(hand)

    print("GAME OVER! Score: " + str(DECK.deck_size() + total_cards_left_in_hands) + '\n')
    player_hands = []
    for player in players:
        player_hands.append(player.cards_in_hand)

    print(GameState(DECK.empty_deck(), piles, player_hands, current_player.name, DECK, final_game_state=True))
