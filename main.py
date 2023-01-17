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

    players = [Player(), Player(), Player(), Player()]

    for player in players:
        player.pick(6, DECK)

    current_player = players[0]

    # for player in players:
    #     player.get_preferences()
    #     determine play
    #     make play
    #     draw new cards
    #     move to next player