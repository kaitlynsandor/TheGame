class GameState:
    def __init__(self, is_game_over, piles, player_hands, current_player, deck):
        self.is_game_over = is_game_over
        self.piles = piles
        self.player_hands = player_hands
        self.current_player = current_player
        self.deck = deck

    def __repr__(self):
        return "CURRENT GAME STATE \n\n" + str(self.piles[0]) + '\n' + str(self.piles[1]) + '\n' + str(self.piles[2]) + \
               '\n' + str(self.piles[3]) + '\n\nPlayer 1 Hand ' + str(self.player_hands[0]) + '\n' + "Player 2 Hand " \
               + str(self.player_hands[1]) + '\n' + "Player 3 Hand " + str(self.player_hands[2]) + '\n' + "Player 4 Hand " \
               + str(self.player_hands[3]) + '\n\n' + "CARDS LEFT IN DECK " + str(self.deck.deck_size()) + '\n' + \
               "PLAYER UP NEXT " + str(self.current_player) +'\n'
