class GameState:
    def __init__(self, is_game_over, piles, player_hands, current_player, deck, final_game_state=False):
        self.is_game_over = is_game_over
        self.piles = piles
        self.player_hands = player_hands
        self.current_player = current_player
        self.deck = deck
        self.final_game_state=final_game_state

    def __repr__(self):
        if self.final_game_state:
            starter = 'FINAL GAME STATE'
        else:
            starter = 'CURRENT GAME STATE'

        string =  starter + " \n\n" + str(self.piles[0]) + '\n' + str(self.piles[1]) + '\n' + str(self.piles[2]) + \
               '\n' + str(self.piles[3]) + '\n\nPlayer 0 Hand ' + str(self.player_hands[0]) + '\n' + "Player 1 Hand " \
               + str(self.player_hands[1]) + '\n' + "Player 2 Hand " + str(self.player_hands[2]) + '\n' + "Player 3 Hand " \
               + str(self.player_hands[3])

        if self.final_game_state:
            return string
        else:
            string += "\n\nCARDS LEFT IN DECK " + str(self.deck.deck_size()) + '\n' + \
               "PLAYER UP NEXT " + str(self.current_player) +'\n'

        return string
