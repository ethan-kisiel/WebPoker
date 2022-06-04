from pypoker.game.game_objects import Player
from pypoker.game_items.default_objects import *
from pypoker.utilities.utils import HandScoringUtil
deck = Deck()
board = Board()
board.draw_flop(deck)
board.draw_turn(deck)
board.draw_river(deck)

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
        
    card_one = Card(0,0)
    card_two = Card(0,0)
    card_one.sync('s_A')
    card_two.sync('s_Q')
    
    hand = (card_one, card_two)
    test_player.set_hand(hand)
    test_player.hand_value(board)
    deck.reset()
    test_straight = deck.get_cards()[0:5]
    
    print('Straight: ')
    print(HandScoringUtil.is_straight(test_straight))