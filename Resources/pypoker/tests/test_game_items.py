from pypoker.game_items.default_items import Deck
test_deck = Deck()

def test_print():
    print(test_deck)

def test_initialization():
    assert len(test_deck.get_cards()) == 52
    
def test_draw_card():
    card = test_deck.r_draw_card()
    card = test_deck.draw_card(0)
    assert len(test_deck.get_cards()) == 50
    
def test_draw_cards():
    cards = test_deck.r_draw_cards(10)
    print(cards)
    assert len(test_deck.get_cards()) == 40