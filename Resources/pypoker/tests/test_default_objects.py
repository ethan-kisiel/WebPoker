from string import capwords
from pypoker.game_items.default_objects import *

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

def test_card_comparison():
    card_one = Card(0, -1)
    card_two = Card(1, 8)
    assert (card_one == card_two) == False
    assert (card_one > card_two) == True
    assert (card_one <= card_two) == False
    
def test_sync_card():
    card = Card(0, -1)
    card_0 = card
    card.sync(str(card))
    assert card == card_0

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
    
    board_out = test_board.get_board()
    test_sync = Card(0,0)
    print(board_out[0])
    test_sync.sync(str(board_out[0]))
    print(test_sync)
   # assert (board_out[0] == test_sync) == True
    
    