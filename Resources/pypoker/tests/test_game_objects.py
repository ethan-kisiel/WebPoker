from pypoker.game.game_objects import Player
from pypoker.game_items.default_objects import Deck
deck = Deck()

test_player = Player()
test_player.set_chips(69.00)
test_player.set_hand(tuple(deck.r_draw_cards(2)))

def test_player_obj():
    print(str(test_player))
    test_player.place_bet(69.00)
    assert test_player.has_chips() == False
    
    test_player.set_button('BB')
    print(test_player)
    assert len(str(test_player).split(',')) == 3
    
    test_player.add_chips(420.00)
    
    assert test_player.get_chips() == 420.00