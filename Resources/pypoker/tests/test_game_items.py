from pypoker.game_items.default_items import Deck, Board
test_deck = Deck()

# Deck tests
def test_print():
    print(test_deck)

def test_initialization():
    assert len(test_deck.get_cards()) == 52
    
def test_draw_card():
    card = test_deck.r_draw_card()
    assert test_deck.get_cards()
    card = test_deck.draw_card(0)
    assert len(test_deck.get_cards()) == 50

def test_draw_cards():
    cards = test_deck.r_draw_cards(10)
    print(cards)
    assert len(test_deck.get_cards()) == 40

# Card tests
def test_card_str_repr():
    test_deck.reset()
    assert str(test_deck.draw_card(0)) == 'c_2'

# Board tests
def test_board():
    test_deck.reset()
    test_board = Board()
    assert str(test_board) == ''
    
    test_board.draw_flop(test_deck)
    print('post-flop board: {}'.format(test_board))
    assert len(test_deck.get_cards()) == 48
    
    assert str(test_board) not in str(test_deck)
    
    test_board.draw_turn(test_deck)
    print('post-turn: {}'.format(test_board))
    
    test_board.draw_river(test_deck)
    print('post-river: {}'.format(test_board))
    assert str(test_board) not in str(test_deck)