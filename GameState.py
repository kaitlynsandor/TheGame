class GameState:
    def __init__(self, is_game_over, piles, player_hands, current_player, deck):
        self.is_game_over = is_game_over
        self.piles = piles
        self.player_hands = player_hands
        self.current_player = current_player
        self.deck = deck